from functools import lru_cache


@lru_cache
def fib(n: int) -> int:
    if n <= 1:
        return 1

    return fib(n - 1) + fib(n - 2)


def gen(max: int):
    idx = 1
    while number := fib(idx):
        if number > max:
            break

        if not number % 2:
            yield number
        idx += 1


if __name__ == "__main__":
    print(sum(gen(4000000)))
