import csv

def get_last_price(filename="price_history.csv"):
    try:
        with open(filename, "r") as f:
            rows = list(csv.DictReader(f))
            if len(rows) < 2:
                return None
            return float(rows[-2]["price"])
    except:
        return None