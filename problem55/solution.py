def reverse_int(n: int):
    return int(str(n)[::-1])


def is_palindrome(string: str):
    return string == string[::-1]


def lychrel_counter(n: int):
    new_result = n + reverse_int(n)
    i = 0

    while not is_palindrome(str(new_result)):
        if i == 50:
            return -1

        new_result = new_result + reverse_int(new_result)
        i += 1

    return i + 1


if __name__ == "__main__":
    count = 0
    for n in range(10_000):
        result = lychrel_counter(n)
        print(n, result)
        if result == -1:
            count += 1

    print(count)
