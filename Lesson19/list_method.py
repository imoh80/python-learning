"""
List Methods

Question:
Practice using append(), pop(), and remove() on a list.
"""

flavors = ["Vanilla", "Caramel"]

print("Original list:")
print(flavors)

# Append
flavors.append("Mint")
print("\nAfter append:")
print(flavors)

# Pop
removed_flavor = flavors.pop()

print("\nRemoved using pop():")
print(removed_flavor)
print(flavors)

# Remove
flavors.remove("Caramel")

print("\nAfter remove():")
print(flavors)