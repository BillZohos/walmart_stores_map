import csv
import json

CSV_FILE = "walmart_store_locations.csv"
JSON_FILE = "walmart_store_locations.json"

def csv_to_json(csv_file, json_file):
    with open(csv_file, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = list(reader)
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    csv_to_json(CSV_FILE, JSON_FILE)
    print(f"Converted {CSV_FILE} to {JSON_FILE}")
