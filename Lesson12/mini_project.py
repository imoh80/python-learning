def create_receipt(customer, drink, quantity, price):
    """Return a formatted coffee shop receipt with the customer's details and total price."""
    total = quantity * price
    formatted_customer = customer.strip().title()
    formatted_drink = drink.title()
    receipt = f"Receipt\n{'-' * 20}\nCustomer: {formatted_customer}\nDrink: {formatted_drink}\nQuantity:  {quantity}\nTotal: ₦{total:.2f}"
    return receipt
receipt = create_receipt(
    "   mary imoh   ",
    "iced caramel latte",
    2,
    4250.5,
)
    
print(receipt)