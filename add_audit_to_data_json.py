import json
import os

base_dir = "E:/dashboard_linea_azul"

with open(os.path.join(base_dir, "data.json"), "r", encoding="utf-8") as f:
    data_json = json.load(f)

with open(os.path.join(base_dir, "audit_dataset.json"), "r", encoding="utf-8") as f:
    audit_data = json.load(f)

data_json["auditoria"] = audit_data

with open(os.path.join(base_dir, "data.json"), "w", encoding="utf-8") as f:
    json.dump(data_json, f, ensure_ascii=False, indent=2)

print("data.json actualizado con la sección de auditoría!")
