def primes(n):
    D = {}
    q = 2
    index = 0
    while index < n:
        if q not in D:
            D[q * q] = [q]
            print(q)
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1
        index += 1

    return q


if __name__ == "__main__":
    print(primes(5))
