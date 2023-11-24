def S(n: int, m: int):
    seq = list(range(2, n + 1))
    for round in range(m):
        print(round, seq)
        min_index = seq.index(min(seq))
        seq[min_index] *= seq[min_index]

    return sum(seq) % 1234567891


if __name__ == "__main__":
    print(S(10**4, 10**6))
