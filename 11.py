INCS = {"n":  (1,0,-1),
        "ne": (0,1,-1),
        "se": (-1,1,0),
        "s":  (-1,0,1),
        "sw": (0,-1,1),
        "nw": (1,-1,0) }

INCS_2D = {'n': (0, 1), 'ne': (1, 1), 'nw': (-1, 1),
           's': (0, -1), 'se': (1, -1), 'sw': (-1, -1),
           'e': (1, 0), 'w': (-1, 0)}


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


def far2D(path):
    curr = (0, 0)
    last = ''
    for p in path:
        now = p
        if (last == 'sw' and now == 'se') or (last == 'nw' and now == 'ne'):
            now = 'e'
        elif (last == 'se' and now == 'sw') or (last == 'ne' and now == 'nw'):
            now = 'w'
        (x, y) = INCS_2D[now]
        curr = (curr[0] + x, curr[1] + y)
        last = now

    return max(abs(curr[0]), abs(curr[1]))


if __name__ == '__main__':
    paths = read_path('11.txt')
    for p in paths:
        print(far(p))
        print("\t-->", far2D(p))
