def welcome():
    print("Welcome to Python!")

welcome()


def square(number):
    return number ** 2

print(square(5))
print(square(10))


def subtract(price, discount):
    return price - discount

final_price = subtract(5000, 750)
print(f"Amount to pay: ₦{final_price:.2f}")


def format_name(first, last):
    return f"{first.title()} {last.title()}"

print(format_name("mary", "imoh"))
print(format_name("john", "doe"))