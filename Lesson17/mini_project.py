"""
Mini Project

Question:
Create a recursive countdown timer that counts down from a given number
and prints "Time's up!" when the countdown reaches zero.
"""


def countdown_timer(seconds):
    """Recursively count down until time is up."""
    if seconds == 0:
        print("Time's up!")
        return

    print(f"{seconds} second(s) remaining...")
    countdown_timer(seconds - 1)


countdown_timer(5)