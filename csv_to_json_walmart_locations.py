import csv
import json

CSV_FILE = "walmart_2018_11_06.csv"
JSON_FILE = "walmart_2018_11_06.json"

# You may need to adjust these field names based on the actual CSV header
ADDRESS_FIELDS = ["address", "city", "state", "zip"]

# Convert CSV to JSON
with open(CSV_FILE, newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open(JSON_FILE, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"Converted {CSV_FILE} to {JSON_FILE}")
