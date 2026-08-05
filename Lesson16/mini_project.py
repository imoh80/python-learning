menu = [
    {"name": "Latte", "price": 4500},
    {"name": "Mocha", "price": 5000},
    {"name": "Espresso", "price": 3500}
]

# Apply a 10% discount to every drink
discounted_menu = list(
    map(
        lambda item: {
            "name": item["name"],
            "price": item["price"] * 0.9
        },
        menu
    )
)

print("Discounted Menu")
print("-" * 20)

for drink in discounted_menu:
    print(f"{drink['name']}: ₦{drink['price']:.2f}")