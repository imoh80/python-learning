def coffee_cart():
    """Demonstrate the nonlocal keyword."""
    current_order = "Espresso"

    def change_order():
        nonlocal current_order
        current_order = "Latte"

    change_order()
    print(f"Current order: {current_order}")


coffee_cart()