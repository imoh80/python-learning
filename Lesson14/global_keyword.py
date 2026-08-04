menu_price = 4500


def update_price(new_price):
    """Update the global menu price."""
    global menu_price
    menu_price = new_price


update_price(5000)

print(f"Updated menu price: ₦{menu_price}")