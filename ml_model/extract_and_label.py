import csv
import os

contracts_dir = os.path.join(os.path.dirname(__file__), "../data/smartbugs-curated")
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
for root, dirs, files in os.walk(contracts_dir):
    for filename in files:
        if filename.endswith(".sol"):
            filepath = os.path.join(root, filename)
            with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
                code = f.read()
                vuln = extract_vuln_type(code)
                data.append([code, vuln])

with open(output_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["code", "label"])
    writer.writerows(data)

print(f"Done. Saved {len(data)} contracts to labeled_data.csv")

