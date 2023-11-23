def primes():
    D = {}
    q = 2
    while 1:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


if __name__ == "__main__":
    index = 1
    for prime in primes():
        if index == 10_001:
            print(prime)
            break
        index += 1
