from playwright.sync_api import sync_playwright
from datetime import datetime
import csv
import os
from config import PRODUCT_URL
from config import PRODUCT_NAME


def collect_product_price():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto(PRODUCT_URL)
        page.wait_for_timeout(5000)

        price_text = page.locator(".formatPrice").first.text_content()

        browser.close()

    # clean price
    price = float(price_text.replace("$", "").replace(",", ""))

    return {
        "timestamp": datetime.now().isoformat(),
        "product": PRODUCT_NAME,
        "price": price,
        "raw_price": price_text
    }

def save_to_csv(data, filename, fieldnames):
    base_dir = os.path.dirname(__file__)
    path = os.path.join(base_dir, filename)
    file_exists = os.path.exists(path)

    with open(path, mode="a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)


import csv

