"""
Base Case

Question:
Demonstrate the importance of a base case in a recursive function.
"""


def greet(number):
    """Print numbers until the base case is reached."""
    if number == 0:
        print("Finished")
        return

    print(number)
    greet(number - 1)


greet(3)