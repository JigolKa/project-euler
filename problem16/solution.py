def get_digits(number: int):
    return [int(x) for x in str(number)]


if __name__ == "__main__":
    print(sum(get_digits(2**1000)))
