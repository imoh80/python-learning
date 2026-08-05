"""
Call Stack

Question:
Use recursion to demonstrate how Python pauses and resumes function calls.
"""


def greet(number):
    """Demonstrate the order in which recursive calls are executed."""
    if number == 0:
        print("Finished")
        return

    print(f"Entering {number}")
    greet(number - 1)
    print(f"Leaving {number}")


greet(3)