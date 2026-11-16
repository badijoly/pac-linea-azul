import csv
import json

base_dir = "E:/dashboard_linea_azul"

# Let's inspect Challwa Q1, Q2, Q3
# What were the correct answers in Challwa?
# Let's look at students with highest scores (e.g., 3/3 on D1, D2, D3 or Total 9/9)
# In Challwa puntajes: Luciana Urapiante, Mateo Torres, Antonella Espinoza, Sebastián Salazar, Fernando Aros had Total POST = 9!
# What did they answer in POST?
with open(f"{base_dir}/raw_challwa_respuestas.csv", "r", encoding="utf-8") as f:
    ch_rows = list(csv.DictReader(f))

perfect_students = ["Luciana Urapiante Bilbao", "Mateo Torres Quispe", "Antonella Espinoza Manuelda", "Sebastián Salazar Tapia", "Fernando Aros Santus"]
print("Perfect POST students in Challwa:")
for r in ch_rows:
    if r["Nombre"] in perfect_students:
        print(f"{r['Nombre']}: Q1 POST={r['Q1 POST']}, Q2 POST={r['Q2 POST']}, Q3 POST={r['Q3 POST']}")

# In Desierto Azul: what were the correct answers for Q1, Q2, Q3 (and B1, B2, B3)?
with open(f"{base_dir}/raw_desierto_azul_respuestas.csv", "r", encoding="utf-8") as f:
    da_rows = list(csv.DictReader(f))

# In DA puntajes: who had D1 POST = 3 and Colillas = 1 (KPI POST = 4)?
# Alan Erazo, Antonia Negrete, Ariana Morales, Luciana Urapiante, etc.
perfect_da = ["Alan Erazo Cuero", "Antonia Negrete Pastén", "Ariana Morales Alpaca", "Luciana Urapiante Bilbao"]
print("\nPerfect POST students in Desierto Azul:")
for r in da_rows:
    if r["Nombre oficial"] in perfect_da:
        print(f"{r['Nombre oficial']}: B1 POST={r['B1 POST']}, B2 POST={r['B2 POST']}, B3 POST={r['B3 POST']}, B4={r['B4 basura+acción (POST)']}")
