def reverse_int(x: int):
    return int(str(x)[::-1])


def only_odd_digits(n: int):
    is_ok = True

    for digit in str(n):
        if int(digit) % 2 == 0:
            is_ok = False
            break

    return is_ok


assert only_odd_digits(13539)
assert not only_odd_digits(1453)

if __name__ == "__main__":
    count = 0
    for n in range(1, 10**9 + 1):
        if only_odd_digits(n + reverse_int(n)):
            print(n + reverse_int(n), n)
            count += 1

    print(count)
