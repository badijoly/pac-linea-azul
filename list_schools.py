import csv

with open("E:/dashboard_linea_azul/raw_challwa_puntajes.csv", "r", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

by_school = {}
for r in rows:
    s = r["Colegio"]
    by_school.setdefault(s, []).append(r["Nombre"])

for s, students in by_school.items():
    print(f"{s} ({len(students)}): {', '.join(students[:3])}...")
