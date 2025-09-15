import requests
from bs4 import BeautifulSoup
import csv
import time

BASE_URL = "https://walmart.supermarketlocationmaps.com/en/usa?page={}"  # Pagination format
OUTPUT_CSV = "walmart_supercenters.csv"

# Columns to extract (update as needed based on actual page structure)
CSV_COLUMNS = ["Store Name", "Address", "City", "State", "Zip"]

def scrape_page(page_num):
    url = BASE_URL.format(page_num)
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    stores = []
    # Find all store entries (update selector as needed)
    for store_div in soup.select("div.store-listing"):  # Example selector
        name = store_div.select_one("h3").get_text(strip=True) if store_div.select_one("h3") else ""
        address = store_div.select_one(".address").get_text(strip=True) if store_div.select_one(".address") else ""
        city = store_div.select_one(".city").get_text(strip=True) if store_div.select_one(".city") else ""
        state = store_div.select_one(".state").get_text(strip=True) if store_div.select_one(".state") else ""
        zip_code = store_div.select_one(".zip").get_text(strip=True) if store_div.select_one(".zip") else ""
        stores.append({
            "Store Name": name,
            "Address": address,
            "City": city,
            "State": state,
            "Zip": zip_code
        })
    return stores

def main():
    all_stores = []
    for page in range(1, 42):  # 41 pages
        print(f"Scraping page {page}...")
        stores = scrape_page(page)
        all_stores.extend(stores)
        time.sleep(1)  # Be polite to the server
    # Write to CSV
    with open(OUTPUT_CSV, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=CSV_COLUMNS)
        writer.writeheader()
        for store in all_stores:
            writer.writerow(store)
    print(f"Scraped {len(all_stores)} stores. Data saved to {OUTPUT_CSV}.")

if __name__ == "__main__":
    main()
