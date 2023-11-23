def check_number(x: int):
    is_compaptible = True

    for n in range(1, 7):
        number = str(x * n)
        if sorted(str(x)) != sorted(number):
            is_compaptible = False

    return is_compaptible


if __name__ == "__main__":
    x = 1
    while not check_number(x):
        x += 1

    print(x)
