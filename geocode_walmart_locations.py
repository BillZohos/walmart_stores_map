import json
import requests
import time

INPUT_JSON = "walmart_store_locations.json"
OUTPUT_JSON = "walmart_store_locations_geocoded.json"
NOMINATIM_URL = "https://nominatim.openstreetmap.org/search"
USER_AGENT = "WalmartMapGeocoder/1.0 (your@email.com)"

# Adjust these field names if needed
ADDRESS_FIELDS = ["Address", "City", "State", "Zip"]

def build_address(entry):
    return ", ".join([str(entry.get(field, "")) for field in ADDRESS_FIELDS if entry.get(field)])

def geocode(address):
    params = {
        "q": address,
        "format": "json",
        "limit": 1
    }
    headers = {"User-Agent": USER_AGENT}
    response = requests.get(NOMINATIM_URL, params=params, headers=headers)
    if response.status_code == 200:
        results = response.json()
        if results:
            return results[0]["lat"], results[0]["lon"]
    return None, None

def main():
    with open(INPUT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    for i, entry in enumerate(data):
        address = build_address(entry)
        lat, lon = geocode(address)
        entry["latitude"] = lat
        entry["longitude"] = lon
        print(f"{i+1}/{len(data)}: {address} -> {lat}, {lon}")
        time.sleep(1)  # Nominatim rate limit: 1 request/sec
    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"Geocoding complete. Results saved to {OUTPUT_JSON}.")

if __name__ == "__main__":
    main()
