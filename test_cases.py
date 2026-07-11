from app import Order, FineTunedFlashSale


def main():

    orders = [
        Order("ORD101", 150),
        Order("ORD102", 60),
        Order("ORD103", 90),
        Order("ORD104", 200),
        Order("ORD105", 110),
        Order("ORD106", 175),
        Order("ORD107", 50),
    ]

    processor = FineTunedFlashSale()

    processor.load_orders(orders)

    print("=" * 50)
    print("ORIGINAL ORDER LIST")
    print("=" * 50)

    print(processor.batch_orders)

    processor.sort_orders_by_value_inplace()

    print("\n" + "=" * 50)
    print("SORTED ORDER LIST")
    print("=" * 50)

    print(processor.batch_orders)

    target = 260

    result = processor.find_budget_pair(target)

    print("\n" + "=" * 50)
    print(f"SEARCHING FOR TARGET BUDGET = ${target}")
    print("=" * 50)

    if result:
        print("Matching Orders Found:")
        print(result[0])
        print(result[1])
    else:
        print("No matching pair found.")


if __name__ == "__main__":
    main()