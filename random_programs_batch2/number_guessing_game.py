"""
Number Guessing Game

Guess the random number. Provides higher/lower hints.
"""

import random
import sys


def main() -> None:
    low = 1
    high = 100
    attempts_limit = 10

    if len(sys.argv) > 1:
        low = int(sys.argv[1])
    if len(sys.argv) > 2:
        high = int(sys.argv[2])
    if len(sys.argv) > 3:
        attempts_limit = int(sys.argv[3])

    if low >= high:
        print("Invalid range: low must be < high.")
        return

    secret = random.randint(low, high)
    attempts = 0

    print(f"I picked a number between {low} and {high}.")

    while attempts < attempts_limit:
        guess_raw = input(f"Attempt {attempts + 1}/{attempts_limit} - Your guess: ").strip()
        try:
            guess = int(guess_raw)
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1
        if guess == secret:
            print(f"Correct! The number was {secret}.")
            return

        if guess < secret:
            print("Too low.")
        else:
            print("Too high.")

    print(f"Out of attempts. The number was {secret}.")


if __name__ == "__main__":
    main()
