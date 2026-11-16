import pymupdf
from rapidocr_onnxruntime import RapidOCR
import json
import os
import re

ocr = RapidOCR()
base_dir = "E:/dashboard_linea_azul"

with open(os.path.join(base_dir, "data.json"), "r", encoding="utf-8") as f:
    data_json = json.load(f)

students = data_json["estudiantes"]
student_names = [s["nombre"] for s in students]

def clean_str(s):
    if not s: return ""
    return re.sub(r'[^a-zA-ZáéíóúñÁÉÍÓÚÑ]', '', s.lower())

def match_student(raw_text):
    clean_text = clean_str(raw_text)
    best_match = None
    best_score = 0
    for name in student_names:
        tokens = name.split()
        matches = sum(1 for t in tokens if len(t) > 2 and clean_str(t) in clean_text)
        score = matches / len(tokens)
        if score > best_score and score >= 0.4:
            best_score = score
            best_match = name
    return best_match, best_score

# Files to process
pdf_catalog = [
    ("hito 3 AM pre Azul.pdf", "Hito 3", "AM", "PRE"),
    ("hito 3 AM post Azul.pdf", "Hito 3", "AM", "POST"),
    ("hito 3 PM pre Azul.pdf", "Hito 3", "PM", "PRE"),
    ("hito 3 PM post Azul.pdf", "Hito 3", "PM", "POST"),
    ("Hito 4 AM pre Azul.pdf", "Hito 4", "AM", "PRE"),
    ("Hito 4 AM post Azul.pdf", "Hito 4", "AM", "POST"),
    ("Hito 4 PM pre Azul.pdf", "Hito 4", "PM", "PRE"),
    ("Hito 4 PM post Azul.pdf", "Hito 4", "PM", "POST"),
]

all_scans = []

for filename, hito, session, timing in pdf_catalog:
    filepath = os.path.join(base_dir, "evaluaciones_escaneadas", filename)
    if not os.path.exists(filepath):
        print(f"Skipping {filename}: not found")
        continue
        
    doc = pymupdf.open(filepath)
    n_pages = len(doc)
    print(f"Scanning {filename} ({n_pages} pages)...")
    
    for i in range(n_pages):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        img_bytes = pix.tobytes("png")
        res, _ = ocr(img_bytes)
        
        lines = [r[1] for r in res] if res else []
        full_text = " ".join(lines)
        
        matched_name, conf = match_student(full_text)
        
        # Detect marked choices
        # For Hito 3: Q1, Q2, Q3
        # Look for patterns like "a)", "b)", "c)", "d)" with checkmarks or letters
        marked_choices = []
        for l in lines:
            m = re.search(r'([a-d])[\)\.]', l.lower())
            if m:
                marked_choices.append(m.group(1))
                
        all_scans.append({
            "pdf": filename,
            "hito": hito,
            "session": session,
            "timing": timing,
            "page": i + 1,
            "matched_student": matched_name,
            "confidence": round(conf, 2),
            "text_preview": full_text[:160],
            "detected_options": marked_choices[:6]
        })
        print(f"[{hito} {session} {timing}] P.{i+1:02d}: {matched_name} (conf={conf:.2f})")

# Save raw audit scan
with open(os.path.join(base_dir, "audit_scans_raw.json"), "w", encoding="utf-8") as f:
    json.dump(all_scans, f, ensure_ascii=False, indent=2)

print(f"\nAudit complete! Total pages scanned: {len(all_scans)}")
