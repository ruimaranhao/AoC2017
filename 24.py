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


def gen_bridges(library, bridge=None):
    l, s, components, a = bridge or (0, 0, set(), 0)

    for b in library[a]:
        print(a, b)
        next = (a, b) if a <= b else (b, a)
        if next not in components:
            new = l+1, s+a+b, (components | {next}), b
            yield new
            yield from gen_bridges(library, new)


def solve(comp):
    return [b[:2] for b in gen_bridges(comp)]


if __name__ == "__main__":
    comp = read_components('puzzles/24.txt')
    solution = solve(comp)
    part1 = sorted(solution, key=lambda x: x[1])[-1][1]
    part2 = sorted(solution)[-1][1]

    print(part1)
    print(part2)

