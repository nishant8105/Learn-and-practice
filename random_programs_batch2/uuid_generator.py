"""
UUID Generator

Generates one or more UUIDs.
"""

import argparse
import uuid


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate UUIDs.")
    parser.add_argument("--count", type=int, default=1, help="How many UUIDs to generate.")
    parser.add_argument(
        "--version",
        type=int,
        choices=[1, 4],
        default=4,
        help="UUID version to generate (1 or 4).",
    )
    args = parser.parse_args()

    count = max(1, args.count)
    for _ in range(count):
        if args.version == 1:
            print(uuid.uuid1())
        else:
            print(uuid.uuid4())


if __name__ == "__main__":
    main()
