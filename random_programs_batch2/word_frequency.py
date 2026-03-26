"""
Word Frequency

Counts word frequencies in a text input.
Provide a file path as the first argument; otherwise uses stdin.
"""

import re
import sys
from collections import Counter
from typing import List, Tuple


def tokenize(text: str) -> List[str]:
    # Words and numbers; keeps it simple and language-agnostic.
    return re.findall(r"[A-Za-z0-9']+", text.lower())


def top_words(text: str, limit: int = 10) -> List[Tuple[str, int]]:
    tokens = tokenize(text)
    counter = Counter(tokens)
    return counter.most_common(limit)


def main() -> None:
    limit = 10
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if len(sys.argv) > 2:
            limit = int(sys.argv[2])

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
    else:
        if len(sys.argv) > 1:
            limit = int(sys.argv[1])
        print("Paste text (Ctrl+Z then Enter to end on Windows):")
        text = sys.stdin.read()

    for word, count in top_words(text, limit=limit):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
