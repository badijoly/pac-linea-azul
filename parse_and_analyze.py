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
            nombre = parts[0]
            colegio = parts[1]
            ch_pre = parts[2]
            ch_post = parts[3]
            ch_mej = parts[4]
            da_kpi = parts[5]
            da_delta = parts[6]
            climaton = parts[7]
            students.append({
                "nombre": nombre,
                "colegio": colegio,
                "ch_pre": ch_pre,
                "ch_post": ch_post,
                "ch_mej": ch_mej,
                "da_kpi": da_kpi,
                "da_delta": da_delta,
                "climaton": climaton
            })

print(f"Total students parsed from base final: {len(students)}")

# 2. Parse Challwa puntajes
ch_puntajes = {}
with open(os.path.join(base_dir, "raw_challwa_puntajes.csv"), "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        ch_puntajes[r["Nombre"].strip()] = r

# 3. Parse Desierto Azul puntajes
da_puntajes = {}
with open(os.path.join(base_dir, "raw_desierto_azul_puntajes.csv"), "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        da_puntajes[r["Nombre oficial"].strip()] = r

# 4. Parse Challwa respuestas
ch_resp = {}
with open(os.path.join(base_dir, "raw_challwa_respuestas.csv"), "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        ch_resp[r["Nombre"].strip()] = r

# 5. Parse Desierto Azul respuestas
da_resp = {}
with open(os.path.join(base_dir, "raw_desierto_azul_respuestas.csv"), "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        da_resp[r["Nombre oficial"].strip()] = r

# 6. Parse Climaton
clim_resp = {}
with open(os.path.join(base_dir, "raw_climaton_respuestas.csv"), "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for r in reader:
        clim_resp[r["Nombre oficial"].strip()] = r

print(f"Challwa puntajes records: {len(ch_puntajes)}")
print(f"DA puntajes records: {len(da_puntajes)}")
print(f"Challwa respuestas records: {len(ch_resp)}")
print(f"DA respuestas records: {len(da_resp)}")
print(f"Climaton respuestas records: {len(clim_resp)}")

# Let's inspect Challwa calculations
# Scale is 0-9. To normalize to 0-5.0: score_norm = (score / 9.0) * 5.0
# Hake gain: g = (POST - PRE) / (9.0 - PRE) for PRE < 9.0
ch_evals = []
for name, p in ch_puntajes.items():
    try:
        pre = float(p["Total PRE"])
        post = float(p["Total POST"])
        delta = post - pre
        # Normalization to 0-5 scale
        pre_norm5 = round((pre / 9.0) * 5.0, 2)
        post_norm5 = round((post / 9.0) * 5.0, 2)
        delta_norm5 = round(post_norm5 - pre_norm5, 2)
        # Hake
        if pre < 9.0:
            hake = (post - pre) / (9.0 - pre)
        else:
            hake = 0.0 if delta >= 0 else -1.0
        
        # Status
        if delta > 0:
            status = "Mejoró"
        elif delta == 0:
            status = "Mantuvo"
        else:
            status = "Retrocedió"
            
        favorable = (status in ["Mejoró", "Mantuvo"])
        
        ch_evals.append({
            "nombre": name,
            "colegio": p["Colegio"].strip(),
            "pre_raw": pre,
            "post_raw": post,
            "delta_raw": delta,
            "pre_norm5": pre_norm5,
            "post_norm5": post_norm5,
            "delta_norm5": delta_norm5,
            "hake": round(hake, 3),
            "status": status,
            "favorable": favorable,
            "d1_pre": int(p["D1 PRE"]),
            "d2_pre": int(p["D2 PRE"]),
            "d3_pre": int(p["D3 PRE"]),
            "d1_post": int(p["D1 POST"]),
            "d2_post": int(p["D2 POST"]),
            "d3_post": int(p["D3 POST"]),
        })
    except Exception as e:
        print(f"Error in Challwa row for {name}: {e}")

# Desierto Azul calculations
# In DA, KPI is 0-4 (D1 0-3 + Colillas 0-1)
# Scale is 0-4. To normalize to 0-5.0: score_norm = (score / 4.0) * 5.0
# Hake gain: g = (POST - PRE) / (4.0 - PRE) for PRE < 4.0
da_evals = []
for name, p in da_puntajes.items():
    if not p["KPI PRE (0-4)"] or not p["KPI POST (0-4)"]:
        continue
    try:
        pre = float(p["KPI PRE (0-4)"])
        post = float(p["KPI POST (0-4)"])
        delta = post - pre
        pre_norm5 = round((pre / 4.0) * 5.0, 2)
        post_norm5 = round((post / 4.0) * 5.0, 2)
        delta_norm5 = round(post_norm5 - pre_norm5, 2)
        
        if pre < 4.0:
            hake = (post - pre) / (4.0 - pre)
        else:
            hake = 0.0 if delta >= 0 else -1.0
            
        if delta > 0:
            status = "Mejoró"
        elif delta == 0:
            status = "Mantuvo"
        else:
            status = "Retrocedió"
            
        favorable = (status in ["Mejoró", "Mantuvo"])
        
        da_evals.append({
            "nombre": name,
            "colegio": p["Colegio"].strip(),
            "pre_raw": pre,
            "post_raw": post,
            "delta_raw": delta,
            "pre_norm5": pre_norm5,
            "post_norm5": post_norm5,
            "delta_norm5": delta_norm5,
            "hake": round(hake, 3),
            "status": status,
            "favorable": favorable,
            "cumple_kpi": p.get("Cumple KPI", "").strip()
        })
    except Exception as e:
        print(f"Error in DA row for {name}: {e}")

print(f"Valid Challwa evals: {len(ch_evals)}")
print(f"Valid DA evals: {len(da_evals)}")

# Metrics for Challwa
ch_mej = sum(1 for e in ch_evals if e["status"] == "Mejoró")
ch_man = sum(1 for e in ch_evals if e["status"] == "Mantuvo")
ch_ret = sum(1 for e in ch_evals if e["status"] == "Retrocedió")
ch_fav = sum(1 for e in ch_evals if e["favorable"])
ch_avg_pre_raw = sum(e["pre_raw"] for e in ch_evals) / len(ch_evals)
ch_avg_post_raw = sum(e["post_raw"] for e in ch_evals) / len(ch_evals)
ch_avg_pre_norm5 = sum(e["pre_norm5"] for e in ch_evals) / len(ch_evals)
ch_avg_post_norm5 = sum(e["post_norm5"] for e in ch_evals) / len(ch_evals)
ch_avg_delta_norm5 = ch_avg_post_norm5 - ch_avg_pre_norm5
ch_hake_valid = [e["hake"] for e in ch_evals if e["pre_raw"] < 9.0]
ch_avg_hake = sum(ch_hake_valid) / len(ch_hake_valid) if ch_hake_valid else 0

print(f"--- CHALLWA (Hito 1) ---")
print(f"Evaluaciones: {len(ch_evals)}")
print(f"Mejoró: {ch_mej} ({ch_mej/len(ch_evals)*100:.1f}%)")
print(f"Mantuvo: {ch_man} ({ch_man/len(ch_evals)*100:.1f}%)")
print(f"Retrocedió: {ch_ret} ({ch_ret/len(ch_evals)*100:.1f}%)")
print(f"Tasa Favorable: {ch_fav}/{len(ch_evals)} = {ch_fav/len(ch_evals)*100:.1f}%")
print(f"Puntaje Raw (0-9): {ch_avg_pre_raw:.2f} -> {ch_avg_post_raw:.2f} (Delta: +{ch_avg_post_raw-ch_avg_pre_raw:.2f})")
print(f"Puntaje Norm (0-5): {ch_avg_pre_norm5:.2f} -> {ch_avg_post_norm5:.2f} (Delta: +{ch_avg_delta_norm5:.2f})")
print(f"Hake G: {ch_avg_hake:.3f}")

# Metrics for Desierto Azul
da_mej = sum(1 for e in da_evals if e["status"] == "Mejoró")
da_man = sum(1 for e in da_evals if e["status"] == "Mantuvo")
da_ret = sum(1 for e in da_evals if e["status"] == "Retrocedió")
da_fav = sum(1 for e in da_evals if e["favorable"])
da_avg_pre_raw = sum(e["pre_raw"] for e in da_evals) / len(da_evals)
da_avg_post_raw = sum(e["post_raw"] for e in da_evals) / len(da_evals)
da_avg_pre_norm5 = sum(e["pre_norm5"] for e in da_evals) / len(da_evals)
da_avg_post_norm5 = sum(e["post_norm5"] for e in da_evals) / len(da_evals)
da_avg_delta_norm5 = da_avg_post_norm5 - da_avg_pre_norm5
da_hake_valid = [e["hake"] for e in da_evals if e["pre_raw"] < 4.0]
da_avg_hake = sum(da_hake_valid) / len(da_hake_valid) if da_hake_valid else 0

print(f"\n--- DESIERTO AZUL (Hito 2) ---")
print(f"Evaluaciones: {len(da_evals)}")
print(f"Mejoró: {da_mej} ({da_mej/len(da_evals)*100:.1f}%)")
print(f"Mantuvo: {da_man} ({da_man/len(da_evals)*100:.1f}%)")
print(f"Retrocedió: {da_ret} ({da_ret/len(da_evals)*100:.1f}%)")
print(f"Tasa Favorable: {da_fav}/{len(da_evals)} = {da_fav/len(da_evals)*100:.1f}%")
print(f"Puntaje Raw (0-4): {da_avg_pre_raw:.2f} -> {da_avg_post_raw:.2f} (Delta: +{da_avg_post_raw-da_avg_pre_raw:.2f})")
print(f"Puntaje Norm (0-5): {da_avg_pre_norm5:.2f} -> {da_avg_post_norm5:.2f} (Delta: +{da_avg_delta_norm5:.2f})")
print(f"Hake G: {da_avg_hake:.3f}")

# Metrics Global Línea Azul
tot_evals = len(ch_evals) + len(da_evals)
tot_mej = ch_mej + da_mej
tot_man = ch_man + da_man
tot_ret = ch_ret + da_ret
tot_fav = ch_fav + da_fav
global_pre_norm5 = (sum(e["pre_norm5"] for e in ch_evals) + sum(e["pre_norm5"] for e in da_evals)) / tot_evals
global_post_norm5 = (sum(e["post_norm5"] for e in ch_evals) + sum(e["post_norm5"] for e in da_evals)) / tot_evals
global_delta_norm5 = global_post_norm5 - global_pre_norm5
global_hake_list = ch_hake_valid + da_hake_valid
global_avg_hake = sum(global_hake_list) / len(global_hake_list) if global_hake_list else 0

print(f"\n--- GLOBAL LÍNEA AZUL (Hito 1 + Hito 2) ---")
print(f"Evaluaciones pareadas totales: {tot_evals}")
print(f"Estudiantes únicos: {len(students)}")
print(f"Mejoró: {tot_mej} ({tot_mej/tot_evals*100:.1f}%)")
print(f"Mantuvo: {tot_man} ({tot_man/tot_evals*100:.1f}%)")
print(f"Retrocedió: {tot_ret} ({tot_ret/tot_evals*100:.1f}%)")
print(f"Tasa Favorable Global: {tot_fav}/{tot_evals} = {tot_fav/tot_evals*100:.1f}%")
print(f"Puntaje Norm (0-5): {global_pre_norm5:.2f} -> {global_post_norm5:.2f} (Delta: +{global_delta_norm5:.2f})")
print(f"Hake G: {global_avg_hake:.3f}")

# By School breakdown
schools = [
    "Escuela Claudio Matte Pérez",
    "Escuela Ecológica Humberto González Echegoyen",
    "Escuela Ecológica Padre Alberto Hurtado",
    "Escuela Javiera Carrera",
    "Escuela Juan Pablo II",
    "Escuela República de Estados Unidos",
    "Escuela República de Italia",
    "Liceo Domingo Herrera Rivera"
]

school_stats = {}
for s in schools:
    s_ch = [e for e in ch_evals if e["colegio"] == s]
    s_da = [e for e in da_evals if e["colegio"] == s]
    s_tot = s_ch + s_da
    
    s_mej = sum(1 for e in s_tot if e["status"] == "Mejoró")
    s_man = sum(1 for e in s_tot if e["status"] == "Mantuvo")
    s_ret = sum(1 for e in s_tot if e["status"] == "Retrocedió")
    s_fav = sum(1 for e in s_tot if e["favorable"])
    
    s_pre = sum(e["pre_norm5"] for e in s_tot) / len(s_tot) if s_tot else 0
    s_post = sum(e["post_norm5"] for e in s_tot) / len(s_tot) if s_tot else 0
    s_delta = s_post - s_pre
    
    s_hake_list = [e["hake"] for e in s_tot]
    s_hake = sum(s_hake_list) / len(s_hake_list) if s_hake_list else 0
    
    school_stats[s] = {
        "n_evals": len(s_tot),
        "ch_evals": len(s_ch),
        "da_evals": len(s_da),
        "mej": s_mej,
        "man": s_man,
        "ret": s_ret,
        "fav": s_fav,
        "pct_fav": round(s_fav / len(s_tot) * 100, 1) if s_tot else 0,
        "pre_norm5": round(s_pre, 2),
        "post_norm5": round(s_post, 2),
        "delta_norm5": round(s_delta, 2),
        "hake": round(s_hake, 3)
    }

print("\n--- DESGLOSE POR ESTABLECIMIENTO (NORMALIZADO 0-5) ---")
for s, st in school_stats.items():
    print(f"{s}: N={st['n_evals']} | Pre={st['pre_norm5']} | Post={st['post_norm5']} | Delta={st['delta_norm5']:+.2f} | Hake={st['hake']} | Fav={st['fav']}/{st['n_evals']} ({st['pct_fav']}%)")
