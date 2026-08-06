# List Comprehension

numbers = [1, 2, 3, 4, 5]

doubled = [num * 2 for num in numbers]

print("Original:", numbers)
print("Doubled:", doubled)

prices = [1000, 2000, 3000]

new_prices = [price + 500 for price in prices]

print("Updated Prices:", new_prices)