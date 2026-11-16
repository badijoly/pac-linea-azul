import pymupdf
from rapidocr_onnxruntime import RapidOCR
import json
import os
import re

ocr = RapidOCR()
base_dir = "E:/dashboard_linea_azul"

# Load students from base
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
        # Check tokens of name
        tokens = name.split()
        matches = sum(1 for t in tokens if len(t) > 2 and clean_str(t) in clean_text)
        score = matches / len(tokens)
        if score > best_score and score >= 0.4:
            best_score = score
            best_match = name
    return best_match, best_score

def scan_pdf(pdf_name, hito_type, session_type, timing_type):
    pdf_path = os.path.join(base_dir, "evaluaciones_escaneadas", pdf_name)
    if not os.path.exists(pdf_path):
        print(f"File not found: {pdf_path}")
        return []
        
    doc = pymupdf.open(pdf_path)
    total_pages = len(doc)
    print(f"\nProcessing {pdf_name} ({total_pages} pages)...")
    
    pages_results = []
    for i in range(total_pages):
        page = doc[i]
        pix = page.get_pixmap(dpi=150)
        img_bytes = pix.tobytes("png")
        res, _ = ocr(img_bytes)
        
        all_lines = [r[1] for r in res] if res else []
        joined_text = " ".join(all_lines)
        
        matched_name, conf = match_student(joined_text)
        
        pages_results.append({
            "page": i + 1,
            "pdf": pdf_name,
            "hito": hito_type,
            "session": session_type,
            "timing": timing_type,
            "matched_student": matched_name,
            "match_confidence": round(conf, 2),
            "text_sample": joined_text[:120],
            "total_lines_detected": len(all_lines)
        })
        
    return pages_results

print("Starting audit script...")
