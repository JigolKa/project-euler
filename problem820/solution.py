from typing import Callable
from decimal import Decimal, getcontext


def d(x: Decimal, base: int) -> Decimal:
    getcontext().prec = base + 1
    parts = str(x).split(".")

    if len(parts) == 1:
        return Decimal(0)

    floating_digits = [int(n) for n in parts[1]]
    if len(floating_digits) < base:
        return Decimal(0)

    return Decimal(floating_digits[base - 1])


def summation(start: int, end: int, lmda: Callable[[int], Decimal]):
    sum = 0

    for idx in range(start, end + 1):
        result = lmda(idx)
        # print(result, end=" ")
        sum += result

    return sum


def S(n: int):
    return summation(1, n, lambda x: d(Decimal(1) / Decimal(x), n))


if __name__ == "__main__":
    print(S(int(input())))
