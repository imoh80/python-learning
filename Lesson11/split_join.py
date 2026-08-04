data = "   mary,latte,4500   "

data = data.strip().split(",")

customer = data[0].title()
drink = data[1].upper()
price = int(data[2])

print(
    f"Receipt\n"
    f"{'-' * 20}\n"
    f"Customer: {customer}\n"
    f"Drink: {drink}\n"
    f"Total: ₦{price:.2f}"
)


user = "   mARY.iMOH@example.COM   "

username, domain = user.strip().lower().split("@")

print(
    f"\nLogin Details\n"
    f"{'-' * 20}\n"
    f"Username: {username}\n"
    f"Domain: {domain}"
)