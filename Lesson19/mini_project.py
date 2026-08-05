"""
Mini Project

Question:
Create a simple coffee shop inventory manager using list methods.
"""

inventory = ["Coffee Beans", "Milk", "Sugar"]

print("☕ COFFEE SHOP INVENTORY")
print("-" * 30)

print("\nCurrent Inventory:")
print(inventory)

# Add a new item
inventory.append("Cups")
print("\nAdded: Cups")
print(inventory)

# Remove the last item
removed_item = inventory.pop()
print(f"\nRemoved with pop(): {removed_item}")
print(inventory)

# Remove by value
inventory.remove("Sugar")
print("\nRemoved: Sugar")
print(inventory)

# Update an item
inventory[1] = "Oat Milk"
print("\nUpdated Milk to Oat Milk")
print(inventory)

# Sort the inventory
inventory.sort()
print("\nSorted Inventory:")
print(inventory)