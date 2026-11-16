import csv
import json

base_dir = "E:/dashboard_linea_azul"

# 1. Challwa accuracy
with open(f"{base_dir}/raw_challwa_respuestas.csv", "r", encoding="utf-8") as f:
    ch_rows = list(csv.DictReader(f))

n_ch = len(ch_rows)
q1_ch_pre = sum(1 for r in ch_rows if r["Q1 PRE"].strip().lower() == "b")
q1_ch_post = sum(1 for r in ch_rows if r["Q1 POST"].strip().lower() == "b")

q2_ch_pre = sum(1 for r in ch_rows if r["Q2 PRE"].strip().lower() == "b")
q2_ch_post = sum(1 for r in ch_rows if r["Q2 POST"].strip().lower() == "b")

q3_ch_pre = sum(1 for r in ch_rows if r["Q3 PRE"].strip().lower() == "b")
q3_ch_post = sum(1 for r in ch_rows if r["Q3 POST"].strip().lower() == "b")

print(f"Challwa Q1 (b): PRE={q1_ch_pre}/{n_ch} ({q1_ch_pre/n_ch*100:.1f}%) -> POST={q1_ch_post}/{n_ch} ({q1_ch_post/n_ch*100:.1f}%)")
print(f"Challwa Q2 (b): PRE={q2_ch_pre}/{n_ch} ({q2_ch_pre/n_ch*100:.1f}%) -> POST={q2_ch_post}/{n_ch} ({q2_ch_post/n_ch*100:.1f}%)")
print(f"Challwa Q3 (b): PRE={q3_ch_pre}/{n_ch} ({q3_ch_pre/n_ch*100:.1f}%) -> POST={q3_ch_post}/{n_ch} ({q3_ch_post/n_ch*100:.1f}%)")

# 2. Desierto Azul accuracy
with open(f"{base_dir}/raw_desierto_azul_respuestas.csv", "r", encoding="utf-8") as f:
    da_rows = list(csv.DictReader(f))

n_da = len(da_rows)
# In DA: Q1 PRE vs B1 POST (correct: d)
q1_da_pre = sum(1 for r in da_rows if "d" in r["Q1 PRE"].strip().lower())
q1_da_post = sum(1 for r in da_rows if "d" in r["B1 POST"].strip().lower())

# Q2 PRE vs B2 POST (correct: d)
q2_da_pre = sum(1 for r in da_rows if "d" in r["Q2 PRE"].strip().lower())
q2_da_post = sum(1 for r in da_rows if "d" in r["B2 POST"].strip().lower())

# Q3 PRE vs B3 POST (correct: a)
q3_da_pre = sum(1 for r in da_rows if "a" in r["Q3 PRE"].strip().lower())
q3_da_post = sum(1 for r in da_rows if "a" in r["B3 POST"].strip().lower())

print(f"\nDesierto Azul Q1 (d): PRE={q1_da_pre}/{n_da} ({q1_da_pre/n_da*100:.1f}%) -> POST={q1_da_post}/{n_da} ({q1_da_post/n_da*100:.1f}%)")
print(f"Desierto Azul Q2 (d): PRE={q2_da_pre}/{n_da} ({q2_da_pre/n_da*100:.1f}%) -> POST={q2_da_post}/{n_da} ({q2_da_post/n_da*100:.1f}%)")
print(f"Desierto Azul Q3 (a): PRE={q3_da_pre}/{n_da} ({q3_da_pre/n_da*100:.1f}%) -> POST={q3_da_post}/{n_da} ({q3_da_post/n_da*100:.1f}%)")

# Colillas identification
with open(f"{base_dir}/raw_desierto_azul_puntajes.csv", "r", encoding="utf-8") as f:
    da_pts_rows = [r for r in csv.DictReader(f) if r["Colillas PRE"]]

col_pre = sum(1 for r in da_pts_rows if r["Colillas PRE"].strip() == "1")
col_post = sum(1 for r in da_pts_rows if r["Colillas POST"].strip() == "1")
n_col = len(da_pts_rows)
print(f"Colillas reconocidas: PRE={col_pre}/{n_col} ({col_pre/n_col*100:.1f}%) -> POST={col_post}/{n_col} ({col_post/n_col*100:.1f}%)")
