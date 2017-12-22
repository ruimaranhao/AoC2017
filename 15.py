def next(prev, factor):
    return (prev * factor) % 2147483647


def next_criteria(prev, factor, criteria):
    res = (prev * factor) % 2147483647
    if res % criteria == 0:
        return res

    return next_criteria(res, factor, criteria)


def jury_count(seedA=65, seedB=8921, trials=40_000_000, part1=True):
    factA = 16807
    factB = 48271

    valueA = seedA
    valueB = seedB

    tries = 0
    count = 0
    while tries < trials:
        if part1:
            valueA = next(valueA, factA)
            valueB = next(valueB, factB)
        else:
            valueA = next_criteria(valueA, factA, 4)
            valueB = next_criteria(valueB, factB, 8)

        if (valueA & 0x0000FFFF) == (valueB & 0x0000FFFF):
            count += 1

        tries += 1

    return count


if __name__ == "__main__":
    genA = 277
    genB = 349

    print(jury_count(genA, genB, trials=5_000_000, part1=False))
