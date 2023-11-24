if __name__ == "__main__":
    for c in range(1000):
        for b in range(1000):
            for a in range(1000):
                if not a < b < c or a**2 + b**2 != c**2:
                    continue

                if a + b + c == 1000:
                    print(a, b, c)
                    break
