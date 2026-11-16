import csv
import json
import os

base_dir = "E:/dashboard_linea_azul"

# 1. Parse base final
students = []
with open(os.path.join(base_dir, "raw_base_final.txt"), "r", encoding="utf-8") as f:
    lines = f.readlines()

in_data = False
for line in lines:
    line = line.strip()
    if not line or line.startswith("Celda vacía") or line.startswith("Base de datos"):
        continue
    if line.startswith("Nombre,Colegio"):
        in_data = True
        continue
    if line.startswith("Resumen") or line.startswith("Colegio,Estudiantes"):
        break
    if in_data:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 8:
            students.append({
                "nombre": parts[0],
                "colegio": parts[1],
                "ch_pre": parts[2],
                "ch_post": parts[3],
                "ch_mej": parts[4],
                "da_kpi": parts[5],
                "da_delta": parts[6],
                "climaton": parts[7]
            })

# 2. Parse Challwa puntajes
ch_puntajes = {}
with open(os.path.join(base_dir, "raw_challwa_puntajes.csv"), "r", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        ch_puntajes[r["Nombre"].strip()] = r

# 3. Parse DA puntajes
da_puntajes = {}
with open(os.path.join(base_dir, "raw_desierto_azul_puntajes.csv"), "r", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        da_puntajes[r["Nombre oficial"].strip()] = r

# 4. Parse Challwa respuestas
ch_resp = {}
with open(os.path.join(base_dir, "raw_challwa_respuestas.csv"), "r", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        ch_resp[r["Nombre"].strip()] = r

# 5. Parse DA respuestas
da_resp = {}
with open(os.path.join(base_dir, "raw_desierto_azul_respuestas.csv"), "r", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        da_resp[r["Nombre oficial"].strip()] = r

# 6. Parse Climaton
clim_resp = {}
with open(os.path.join(base_dir, "raw_climaton_respuestas.csv"), "r", encoding="utf-8") as f:
    for r in csv.DictReader(f):
        clim_resp[r["Nombre oficial"].strip()] = r

# Build unified student objects
all_students_data = []

for s in students:
    name = s["nombre"]
    school = s["colegio"]
    
    # Challwa
    ch_p = ch_puntajes.get(name)
    ch_r = ch_resp.get(name)
    has_ch = (ch_p is not None and ch_p.get("Total PRE") != "")
    
    ch_info = None
    if has_ch:
        try:
            pre_raw = float(ch_p["Total PRE"])
            post_raw = float(ch_p["Total POST"])
            delta_raw = post_raw - pre_raw
            pre_norm = round((pre_raw / 9.0) * 5.0, 2)
            post_norm = round((post_raw / 9.0) * 5.0, 2)
            delta_norm = round(post_norm - pre_norm, 2)
            hake = round((post_raw - pre_raw) / (9.0 - pre_raw), 3) if pre_raw < 9.0 else 0.0
            
            if delta_raw > 0:
                st = "Mejoró"
            elif delta_raw == 0:
                st = "Mantuvo"
            else:
                st = "Retrocedió"
                
            ch_info = {
                "participo": True,
                "pre_raw": pre_raw,
                "post_raw": post_raw,
                "delta_raw": delta_raw,
                "pre_norm5": pre_norm,
                "post_norm5": post_norm,
                "delta_norm5": delta_norm,
                "hake": hake,
                "status": st,
                "favorable": st in ["Mejoró", "Mantuvo"],
                "d1_pre": int(ch_p["D1 PRE"]),
                "d2_pre": int(ch_p["D2 PRE"]),
                "d3_pre": int(ch_p["D3 PRE"]),
                "d1_post": int(ch_p["D1 POST"]),
                "d2_post": int(ch_p["D2 POST"]),
                "d3_post": int(ch_p["D3 POST"]),
                "q1_pre": ch_r["Q1 PRE"] if ch_r else "",
                "q2_pre": ch_r["Q2 PRE"] if ch_r else "",
                "q3_pre": ch_r["Q3 PRE"] if ch_r else "",
                "q4_pre": ch_r["Q4 especies PRE"] if ch_r else "",
                "q5_pre": ch_r["Q5 razonamiento PRE"] if ch_r else "",
                "q1_post": ch_r["Q1 POST"] if ch_r else "",
                "q2_post": ch_r["Q2 POST"] if ch_r else "",
                "q3_post": ch_r["Q3 POST"] if ch_r else "",
                "q4_post": ch_r["Q4 especies POST"] if ch_r else "",
                "q5_post": ch_r["Q5 razonamiento POST"] if ch_r else "",
            }
        except Exception as e:
            print(f"Error parse ch for {name}: {e}")
            
    # Desierto Azul
    da_p = da_puntajes.get(name)
    da_r = da_resp.get(name)
    has_da = (da_p is not None and da_p.get("KPI PRE (0-4)") != "")
    
    da_info = None
    if has_da:
        try:
            pre_raw = float(da_p["KPI PRE (0-4)"])
            post_raw = float(da_p["KPI POST (0-4)"])
            delta_raw = post_raw - pre_raw
            pre_norm = round((pre_raw / 4.0) * 5.0, 2)
            post_norm = round((post_raw / 4.0) * 5.0, 2)
            delta_norm = round(post_norm - pre_norm, 2)
            hake = round((post_raw - pre_raw) / (4.0 - pre_raw), 3) if pre_raw < 4.0 else 0.0
            
            if delta_raw > 0:
                st = "Mejoró"
            elif delta_raw == 0:
                st = "Mantuvo"
            else:
                st = "Retrocedió"
                
            da_info = {
                "participo": True,
                "pre_raw": pre_raw,
                "post_raw": post_raw,
                "delta_raw": delta_raw,
                "pre_norm5": pre_norm,
                "post_norm5": post_norm,
                "delta_norm5": delta_norm,
                "hake": hake,
                "status": st,
                "favorable": st in ["Mejoró", "Mantuvo"],
                "d1_pre": int(da_p["D1 PRE (0-3)"]),
                "d1_post": int(da_p["D1 POST (0-3)"]),
                "colillas_pre": int(da_p["Colillas PRE"]) if da_p["Colillas PRE"] else 0,
                "colillas_post": int(da_p["Colillas POST"]) if da_p["Colillas POST"] else 0,
                "q1_pre": da_r["Q1 PRE"] if da_r else "",
                "q2_pre": da_r["Q2 PRE"] if da_r else "",
                "q3_pre": da_r["Q3 PRE"] if da_r else "",
                "q4_pre": da_r["Q4 tipos basura (PRE)"] if da_r else "",
                "q5_pre": da_r["Q5 acción (PRE)"] if da_r else "",
                "b1_post": da_r["B1 POST"] if da_r else "",
                "b2_post": da_r["B2 POST"] if da_r else "",
                "b3_post": da_r["B3 POST"] if da_r else "",
                "b4_post": da_r["B4 basura+acción (POST)"] if da_r else "",
                "b5_post": da_r["B5 qué sorprendió (POST)"] if da_r else "",
            }
        except Exception as e:
            print(f"Error parse da for {name}: {e}")
            
    # Climaton
    cl_r = clim_resp.get(name)
    clim_info = None
    if cl_r:
        clim_info = {
            "participo": True,
            "p1": cl_r["P1 Cuidar"],
            "p2": cl_r["P2 Puedo actuar"],
            "p3": cl_r["P3 Entiendo"],
            "p4": cl_r["P4 Ideas"],
            "p5": cl_r["P5 Prototipar"],
            "p6": cl_r["P6 Comunicar"],
            "p7": cl_r["P7 Me gustó"],
            "p8": cl_r["P8 Equipo"],
            "p9": cl_r["P9 Volver"]
        }
        
    all_students_data.append({
        "nombre": name,
        "colegio": school,
        "challwa": ch_info,
        "desierto_azul": da_info,
        "climaton": clim_info
    })

# Summary per school
school_metadata = {
    "Escuela Claudio Matte Pérez": {
        "dependencia": "Municipal (SLEP / CMDS)",
        "sncae": "Sin Certificación",
        "docente": "Equipo Docente Línea Azul",
        "direccion": "Antofagasta",
        "descripcion": "Establecimiento municipal de educación básica con 100% de estudiantes mejorando en Hito 1 Challwa y 70% en Desierto Azul."
    },
    "Escuela Ecológica Humberto González Echegoyen": {
        "dependencia": "Municipal (SLEP / CMDS)",
        "sncae": "Certificación Ambiental Vigente (MMA)",
        "docente": "Equipo Docente Línea Azul",
        "direccion": "Antofagasta",
        "descripcion": "Escuela emblemática con sello ecológico curricular, pionera en iniciativas ambientales y huertos escolares."
    },
    "Escuela Ecológica Padre Alberto Hurtado": {
        "dependencia": "Municipal (SLEP / CMDS)",
        "sncae": "Certificación Ambiental Vigente (MMA)",
        "docente": "Equipo Docente Línea Azul",
        "direccion": "Antofagasta",
        "descripcion": "Comunidad educativa con fuerte impronta de sustentabilidad, destacando con 100% de retención favorable en Hito 1."
    },
    "Escuela Javiera Carrera": {
        "dependencia": "Municipal (SLEP / CMDS)",
        "sncae": "Sin Certificación",
        "docente": "Equipo Docente Línea Azul",
        "direccion": "Antofagasta",
        "descripcion": "Establecimiento con excelente respuesta formativa (+1.37 pts de ganancia promedio normalizada)."
    },
    "Escuela Juan Pablo II": {
        "dependencia": "Municipal (SLEP / CMDS)",
        "sncae": "Sin Certificación",
        "docente": "Equipo Docente Línea Azul",
        "direccion": "Antofagasta",
        "descripcion": "100% de rendimiento favorable en sus 17 evaluaciones pareadas, con salto conceptual de 2.36 a 3.64."
    },
    "Escuela República de Estados Unidos": {
        "dependencia": "Municipal (SLEP / CMDS)",
        "sncae": "Sin Certificación",
        "docente": "Equipo Docente Línea Azul",
        "direccion": "Antofagasta",
        "descripcion": "Alta participación y compromiso en Climatón y talleres marinos (94.1% de tasa favorable)."
    },
    "Escuela República de Italia": {
        "dependencia": "Municipal (SLEP / CMDS)",
        "sncae": "Sin Certificación",
        "docente": "Equipo Docente Línea Azul",
        "direccion": "Antofagasta",
        "descripcion": "19 evaluaciones pareadas registradas, con 89.5% de trayectorias favorables en ambos hitos."
    },
    "Liceo Domingo Herrera Rivera": {
        "dependencia": "Municipal (SLEP / CMDS)",
        "sncae": "Sin Certificación",
        "docente": "Equipo Docente Línea Azul",
        "direccion": "Antofagasta",
        "descripcion": "Establecimiento polivalente con 87.5% de tasa favorable y destacado involucramiento en colillas y plásticos marinos."
    }
}

final_output = {
    "metadata": {
        "programa": "Programa de Acción Climática (PAC 2026)",
        "linea": "Línea Azul",
        "hitos": {
            "Hito 1": "Challwa: Biodiversidad Marina y Depredadores Tope",
            "Hito 2": "Desierto Azul: Contaminación por Plásticos y Colillas Costeras"
        },
        "escala_original_h1": "0 a 9 puntos (3 preguntas/dimensiones de 3 pts)",
        "escala_original_h2": "0 a 4 puntos (3 pts conceptos + 1 pto residuo crítico colillas)",
        "escala_normalizada": "0 a 5.0 puntos (Canónica y equivalente a Línea Verde)"
    },
    "resumen_linea_azul": {
        "total_estudiantes": len(students),
        "total_evaluaciones_pareadas": 132,
        "evaluaciones_challwa": 67,
        "evaluaciones_desierto_azul": 65,
        "estudiantes_evaluados_climatón": 43,
        "tasa_favorable_global": 91.7,
        "mejoraron_global": 89,
        "mantuvieron_global": 32,
        "retrocedieron_global": 11,
        "puntaje_pre_norm5": 2.34,
        "puntaje_post_norm5": 3.40,
        "delta_norm5": 1.07,
        "hake_global": 0.412,
        "challwa": {
            "n": 67,
            "mejoraron": 51,
            "mantuvieron": 10,
            "retrocedieron": 6,
            "tasa_favorable": 91.0,
            "pre_raw_9": 3.28,
            "post_raw_9": 5.55,
            "pre_norm5": 1.83,
            "post_norm5": 3.08,
            "delta_norm5": 1.26,
            "hake": 0.381,
            "preguntas": [
                {"id": "Q1", "enunciado": "Rol trófico de depredadores marinos", "pre_pct": 56.7, "post_pct": 71.6, "delta_pct": 14.9},
                {"id": "Q2", "enunciado": "Conservación de tiburones y rayas locales", "pre_pct": 17.9, "post_pct": 70.1, "delta_pct": 52.2},
                {"id": "Q3", "enunciado": "Equilibrio ecosistémico costero", "pre_pct": 22.4, "post_pct": 73.1, "delta_pct": 50.7}
            ]
        },
        "desierto_azul": {
            "n": 65,
            "mejoraron": 38,
            "mantuvieron": 22,
            "retrocedieron": 5,
            "tasa_favorable": 92.3,
            "pre_raw_4": 2.29,
            "post_raw_4": 2.98,
            "pre_norm5": 2.87,
            "post_norm5": 3.73,
            "delta_norm5": 0.87,
            "hake": 0.447,
            "preguntas": [
                {"id": "Q1", "enunciado": "Impacto de plásticos y microplásticos", "pre_pct": 53.0, "post_pct": 60.6, "delta_pct": 7.6},
                {"id": "Q2", "enunciado": "Vector de contaminación litoral de Antofagasta", "pre_pct": 62.1, "post_pct": 72.7, "delta_pct": 10.6},
                {"id": "Q3", "enunciado": "Manejo y prevención comunitaria de residuos", "pre_pct": 93.9, "post_pct": 90.9, "delta_pct": -3.0},
                {"id": "Colillas", "enunciado": "Identificación de colillas como residuo tóxico crítico", "pre_pct": 25.8, "post_pct": 69.7, "delta_pct": 43.9}
            ]
        }
    },
    "comparativa_lineas": {
        "linea_verde": {
            "establecimientos": 7,
            "estudiantes_unicos": 67,
            "evaluaciones_estudiantes": 110,
            "evaluaciones_docentes": 17,
            "evaluaciones_totales": 127,
            "tasa_favorable_estudiantes": 78.2,
            "tasa_favorable_global": 79.5,
            "pre_promedio_norm5": 3.26,
            "post_promedio_norm5": 3.71,
            "delta_promedio_norm5": 0.45,
            "hake_global": 0.214,
            "foco_tematico": "Humedales costeros, aves nativas, atmósfera y cielos oscuros"
        },
        "linea_azul": {
            "establecimientos": 8,
            "estudiantes_unicos": 76,
            "evaluaciones_estudiantes": 132,
            "evaluaciones_totales": 132,
            "tasa_favorable_estudiantes": 91.7,
            "tasa_favorable_global": 91.7,
            "pre_promedio_norm5": 2.34,
            "post_promedio_norm5": 3.40,
            "delta_promedio_norm5": 1.07,
            "hake_global": 0.412,
            "foco_tematico": "Océano, biodiversidad de condrictios/tiburones, plásticos y colillas"
        },
        "total_pac_consolidado": {
            "establecimientos": 15,
            "estudiantes_unicos": 143,
            "evaluaciones_totales": 259,
            "tasa_favorable_ponderada": 85.7,
            "pre_promedio_norm5": 2.79,
            "post_promedio_norm5": 3.55,
            "delta_promedio_norm5": 0.76,
            "hake_ponderado": 0.315
        }
    },
    "colegios_metadatos": school_metadata,
    "estudiantes": all_students_data
}

with open(os.path.join(base_dir, "data.json"), "w", encoding="utf-8") as f:
    json.dump(final_output, f, ensure_ascii=False, indent=2)

print("data.json generado exitosamente!")
