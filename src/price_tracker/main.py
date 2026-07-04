from collector import collect_product_price


def main():
    print("Starting price tracker...")
    collect_product_price()
    price = collect_product_price()
    print(f"Collected data")


if __name__ == "__main__":
    main()