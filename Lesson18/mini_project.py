"""
Mini Project

Question:
Create a coffee shop menu using a list.
Display the full menu, the first drink, the last drink,
and the first three drinks using slicing.
"""

menu = [
    "Latte",
    "Mocha",
    "Espresso",
    "Cappuccino",
    "Americano",
    "Macchiato"
]

print("☕ COFFEE SHOP MENU")
print("-" * 25)

print("Full Menu:")
print(menu)

print("\nFirst Drink:")
print(menu[0])

print("\nLast Drink:")
print(menu[-1])

print("\nFirst Three Drinks:")
print(menu[:3])