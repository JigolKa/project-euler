def seq(n: int):
    for index in range(1, n + 1):
        yield index**index


if __name__ == "__main__":
    digits = str(sum(seq(1000)))
    print(digits)
