import os
import csv

# Absolute paths from the ml_model folder
contracts_dir = os.path.join(os.path.dirname(__file__), "../data/raw_contracts")
output_csv = os.path.join(os.path.dirname(__file__), "../data/processed_contracts/labeled_data.csv")

def extract_vuln_type(code):
    lines = code.split("\n")
    for line in lines:
        if "<report>" in line:
            try:
                vuln = line.strip().split()[-1]
                return vuln.upper()
            except:
                continue
    return "UNKNOWN"

data = []
for filename in os.listdir(contracts_dir):
    if filename.endswith(".sol"):
        filepath = os.path.join(contracts_dir, filename)
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            code = f.read()
            vuln = extract_vuln_type(code)
            data.append([code, vuln])

with open(output_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["code", "label"])
    writer.writerows(data)

print(f"✅ Done. Saved {len(data)} contracts to labeled_data.csv")
