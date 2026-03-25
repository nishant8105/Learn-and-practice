"""
Prime Factorization

Factors an integer into primes using trial division.
"""

import sys
from typing import Dict


def factorize(n: int) -> Dict[int, int]:
    if n == 0:
        raise ValueError("0 cannot be factorized into primes.")

    factors: Dict[int, int] = {}

    # Handle negative numbers: factors of -1 and abs(n).
    if n < 0:
        factors[-1] = 1
        n = -n

    # Trial division.
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 1 if d == 2 else 2  # 2, then only odd numbers

    if n > 1:
        factors[n] = factors.get(n, 0) + 1

    return dict(sorted(factors.items()))


def main() -> None:
    # Usage:
    #   python prime_factorization.py 84
    # or run and type the number when prompted.
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input("Enter an integer: ").strip())

    factors = factorize(n)
    if not factors:
        print("No prime factors found.")
        return

    parts = []
    for prime, exp in factors.items():
        if exp == 1:
            parts.append(str(prime))
        else:
            parts.append(f"{prime}^{exp}")

    print(" * ".join(parts))


if __name__ == "__main__":
    main()
