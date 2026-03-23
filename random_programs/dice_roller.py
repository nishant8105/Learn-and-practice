"""Dice Roller - Simulates rolling one or multiple dice."""

import random


def roll_dice(num_dice=2, sides=6):
    """Roll num_dice dice, each with sides faces. Returns list of results."""
    return [random.randint(1, sides) for _ in range(num_dice)]


if __name__ == "__main__":
    rolls = roll_dice(2, 6)
    print(f"Rolled 2d6: {rolls} | Total: {sum(rolls)}")
