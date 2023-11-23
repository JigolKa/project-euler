def is_palindrome(string: str):
    return string == string[::-1]


def brute_force(start: int, end: int):
    largest = 0
    for n in range(start, end):
        for m in range(start, end):
            product = n * m
            if is_palindrome(str(product)) and product > largest:
                largest = product

    return largest


if __name__ == "__main__":
    print(brute_force(100, 999))
