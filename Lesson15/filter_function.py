prices = [1500, 5000, 3200, 6000]

cheap_prices = list(filter(lambda price: price < 4000, prices))

print(cheap_prices)