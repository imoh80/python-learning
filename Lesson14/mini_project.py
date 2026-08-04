daily_sales = 0


def record_order(customer, drink, quantity, price):
    """Return a receipt and update total daily sales."""
    global daily_sales

    total = quantity * price
    daily_sales += total

    receipt = (
        f"Receipt\n"
        f"{'-' * 20}\n"
        f"Customer: {customer.strip().title()}\n"
        f"Drink: {drink.strip().title()}\n"
        f"Quantity: {quantity}\n"
        f"Total: ₦{total:.2f}"
    )

    return receipt


print(record_order("mary imoh", "latte", 2, 4250))
print()
print(record_order("john doe", "mocha", 1, 3500))
print()
print(f"Daily Sales: ₦{daily_sales:.2f}")