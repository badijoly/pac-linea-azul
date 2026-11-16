import pymupdf
from rapidocr_onnxruntime import RapidOCR
import re

ocr = RapidOCR()

def audit_pdf_names(pdf_path, max_pages=None):
    doc = pymupdf.open(pdf_path)
    total = len(doc) if max_pages is None else min(len(doc), max_pages)
    print(f"\nAuditing {pdf_path} ({total} pages):")
    
    pages_info = []
    for i in range(total):
        page = doc[i]
        # Crop header: top 35% of the page where title, name, school are located
        rect = page.rect
        header_rect = pymupdf.Rect(rect.x0, rect.y0, rect.x1, rect.y0 + rect.height * 0.35)
        pix = page.get_pixmap(clip=header_rect, dpi=200)
        img_bytes = pix.tobytes("png")
        
        res, _ = ocr(img_bytes)
        text_lines = [r[1] for r in res] if res else []
        joined = " | ".join(text_lines)
        
        # Try to find Name after "Nombre:" or in lines
        name = "DESCONOCIDO"
        school = "DESCONOCIDO"
        
        for idx, l in enumerate(text_lines):
            l_clean = l.lower()
            if "nombre" in l_clean:
                # Check next line or same line
                part = l.split(":")[-1].strip()
                if part and part.lower() != "nombre":
                    name = part
                elif idx + 1 < len(text_lines):
                    name = text_lines[idx + 1].strip()
            if "establecimiento" in l_clean or "colegio" in l_clean or "escuela" in l_clean:
                part = l.split(":")[-1].strip()
                if part and len(part) > 3:
                    school = part
                elif idx + 1 < len(text_lines):
                    school = text_lines[idx + 1].strip()
                    
        pages_info.append({
            "page": i + 1,
            "raw_text": joined,
            "detected_name": name,
            "detected_school": school
        })
        print(f"P.{i+1:02d}: Name='{name}' | School='{school}' | Header={joined[:60]}...")
        
    return pages_info

am_info = audit_pdf_names("E:/dashboard_linea_azul/evaluaciones_escaneadas/hito 3 AM pre Azul.pdf", max_pages=15)
