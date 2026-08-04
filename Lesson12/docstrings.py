def format_name(first, last):
    """Return the formatted first and last name separated by a space."""

    full_name = first.title() + " " + last.title()
    return full_name


print(format_name("mary", "imoh"))


def calculate_average(total, count):
    """Return the average of two numbers."""

    return total / count


print(calculate_average(80, 4))