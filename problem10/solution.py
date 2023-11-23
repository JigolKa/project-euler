def primes(n: int):
    D = {}
    q = 2

    while q <= n:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


if __name__ == "__main__":
    print(sum(primes(2_000_000)))
