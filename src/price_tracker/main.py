from collector import collect_product_price, save_to_csv
from notifier import send_email
from analysis import get_last_price


def main():
    print("Starting price tracker...")
    data = collect_product_price()
    save_to_csv(data, "price_history.csv", fieldnames=["timestamp", "product", "price", "raw_price"])
    
    last_price = get_last_price()

    current_price = data["price"]

    if last_price is None:
        message = f"First run. Price is {current_price}"
    else:
        diff = current_price - last_price

        if diff < 0:
            message = f"🔥 PRICE DROPPED by ${abs(diff):.2f}\nNow: {current_price}"
        elif diff > 0:
            message = f"⚠️ Price increased by ${diff:.2f}\nNow: {current_price}"
        else:
            message = f"No change. Price: {current_price}"

    print(message)

    send_email(
        subject="Lenovo Price Update",
        body=message
    )


if __name__ == "__main__":
    main()