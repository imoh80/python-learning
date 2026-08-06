class Laptop:

    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

laptop1 = Laptop("HP", "16GB", "512GB")
laptop2 = Laptop("Dell", "32GB", "1TB")

print("Laptop 1")
print(f"Brand: {laptop1.brand}")
print(f"RAM: {laptop1.ram}")
print(f"Storage: {laptop1.storage}")

print()

print("Laptop 2")
print(f"Brand: {laptop2.brand}")
print(f"RAM: {laptop2.ram}")
print(f"Storage: {laptop2.storage}")