menu = [
    {"name": "Mocha", "price": 5000},
    {"name": "Espresso", "price": 3500},
    {"name": "Latte", "price": 4500}
]

sorted_menu = sorted(menu, key=lambda item: item["price"])

print(sorted_menu)