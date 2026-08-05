"""
Recursion Basics

Question:
Write a recursive function that counts down from a given number to 1,
then prints "Done!" when it reaches 0.
"""


def count_down(number):
    """Count down recursively until the base case is reached."""
    if number <= 0:
        print("Done!")
        return

    print(number)
    count_down(number - 1)


count_down(5)