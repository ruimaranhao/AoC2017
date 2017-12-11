INCS = {"n":  (1,0,-1),
        "ne": (0,1,-1),
        "se": (-1,1,0),
        "s":  (-1,0,1),
        "sw": (0,-1,1),
        "nw": (1,-1,0)}


def read_path(name):
    with open(name, 'r') as f:
        paths = f.readlines()
    return list(map(lambda s: s.strip().split(","), paths))


def far(path):
    def __far(t):
        return max(abs(t[0]), abs(t[1]), abs(t[2]))

    curr = (0, 0, 0)
    furthest = 0
    for p in path:
        (x, y, z) = INCS[p]
        curr = (curr[0] + x, curr[1] + y, curr[2] + z)
        furthest = __far(curr) if __far(curr) > furthest else furthest

    return __far(curr), furthest


if __name__ == '__main__':
    paths = read_path('11.txt')
    for p in paths:
        print(far(p))
