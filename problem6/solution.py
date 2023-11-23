def sum_squares(n: int):
    def generator():
        for index in range(1, n + 1):
            yield index**2

    return sum(generator())


def squared_sum(n: int):
    sum_digits = sum(range(1, n + 1))
    return sum_digits**2


if __name__ == "__main__":
    n = 100
    print(squared_sum(n) - sum_squares(n))
