from playwright.sync_api import sync_playwright
from config import PRODUCT_URL


def collect_product_title():
    """Open the product page and return the page title."""

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(PRODUCT_URL)
        title = page.title()
        browser.close()

    return title

def collect_product_page():

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(PRODUCT_URL)
        page.wait_for_load_state("networkidle")
        input("Inspect the page, then press Enter...")
        browser.close()

    return title

def collect_product_price():
    print("Starting Playwright...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        print("Browser launched.")
        page = browser.new_page()
        print("Navigating to page...")
        page.goto(PRODUCT_URL)
        print("Waiting 5 seconds...")
        page.wait_for_timeout(5000)
        print("Looking for price...")
        price = page.locator(".formatPrice").first.text_content()
        print(f"Price found: {price}")
        browser.close()

    return price