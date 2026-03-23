"""Countdown Timer - Simple countdown in seconds."""

import time


def countdown(seconds):
    """Count down from seconds to 0."""
    for remaining in range(seconds, 0, -1):
        mins, secs = divmod(remaining, 60)
        print(f"\rTime left: {mins:02d}:{secs:02d}", end="", flush=True)
        time.sleep(1)
    print("\nDone!")


if __name__ == "__main__":
    countdown(5)  # 5 second demo
