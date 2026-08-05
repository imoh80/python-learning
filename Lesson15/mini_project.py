menu = [
    {"name": "Latte", "price": 4500},
    {"name": "Mocha", "price": 5000},
    {"name": "Espresso", "price": 3500},
    {"name": "Americano", "price": 3000}
]

# Increase all prices by ₦500
updated_prices = list(
    map(
        lambda item: {
            "name": item["name"],
            "price": item["price"] + 500
        },
        menu
    )
)

# Keep drinks costing ₦4500 or less
affordable_drinks = list(
    filter(
        lambda item: item["price"] <= 4500,
        updated_prices
    )
)

# Sort drinks by price
sorted_menu = sorted(
    affordable_drinks,
    key=lambda item: item["price"]
)

print("Updated Menu")
print("-" * 20)

for drink in sorted_menu:
    print(f"{drink['name']}: ₦{drink['price']}")