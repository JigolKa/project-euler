from functools import lru_cache


@lru_cache
def fib(n: int):
    if n <= 2:
        return 1

    return fib(n - 1) + fib(n - 2)


def check(digits: int):
    index = 1
    while number := fib(index):
        if len(str(number)) == digits:
            return index
        index += 1


if __name__ == "__main__":
    print(check(1000))
