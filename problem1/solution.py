def find_multiple(n: int):
    index = 1
    while index < n:
        if not index % 3 or not index % 5:
            yield index
        index += 1


if __name__ == "__main__":
    print(sum(find_multiple(1000)))
