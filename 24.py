def read_components(name):
    def add(d, key, val):
        if key not in d:
            d[key] = set([val])
        else:
            d[key].add(val)

    d1 = {}
    with open(name, 'r') as f:
        for line in f:
            l, r = tuple(map(int, line.strip().split("/")))
            add(d1, l, r)
            add(d1, r, l)
    return d1


def bridges(lib, bridge=(0, 0, set(), 0)):
    min_max = lambda a, b: (a, b) if a <= b else (b, a)

    num, s, components, a = bridge
    for rhs in lib[a]:
        nxt = min_max(a, rhs)
        if nxt not in components:
            new = num + 1, s + a + rhs, components | {nxt}, rhs
            yield new
            yield from bridges(lib, new)


if __name__ == "__main__":
    library = read_components('puzzles/24.txt')

    part1 = sorted(bridges(library), key=lambda x: x[1])[-1][1]
    print(part1)

    part2 = sorted(bridges(library))[-1][1]
    print(part2)

