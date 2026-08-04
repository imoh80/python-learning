customer = "John"
drink = "Mocha"
price = 3500

print(f"Order for {customer}: {drink} - ₦{price:.2f}")


customer = "   jAnE doE   "
drink = "iced caramel latte"
price = 4250.5

customer = customer.strip().title()
drink = drink.title()

print(
    f"Receipt\n"
    f"{'-' * 20}\n"
    f"Customer: {customer}\n"
    f"Drink: {drink}\n"
    f"Total: ₦{price:.2f}"
)