def create_order(customer, drink, quantity, price, size="Medium"):
    """Return a formatted coffee shop receipt."""

    total = quantity * price
    formatted_customer = customer.strip().title()
    formatted_drink = drink.strip().title()

    receipt = (
        f"Receipt\n"
        f"{'-' * 20}\n"
        f"Customer: {formatted_customer}\n"
        f"Drink: {formatted_drink}\n"
        f"Size: {size}\n"
        f"Quantity: {quantity}\n"
        f"Total: ₦{total:.2f}"
    )

    return receipt


receipt1 = create_order("mary imoh", "latte", 2, 4250, "Large")
receipt2 = create_order("john doe", "mocha", 1, 3500)

print(receipt1)
print()
print(receipt2)