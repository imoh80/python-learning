def add_tax(price):
    """Return the price after adding ₦500 tax."""
    return price + 500


tax = lambda price: price + 500

print(add_tax(4500))
print(tax(4500))