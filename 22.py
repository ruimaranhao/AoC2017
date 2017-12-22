def read_puzzle(name):
    puzzle = {}
    lx = 0
    ly = 0
    with open(name, 'r') as f:
        for line in enumerate(f):
            lx += 1
            _line = list(enumerate(line[1].strip()))
            ly = 0
            for y,c in _line:
                ly += 1
                puzzle[(line[0],y)] = c
    return puzzle, lx, ly


def print_puzzle(puzzle):

    minx = min({x for (x, y) in puzzle})
    maxx = max({x for (x, y) in puzzle})

    miny = min({y for (x, y) in puzzle})
    maxy = max({y for (x, y) in puzzle})

    for i in range(minx, maxx + 1):
        for j in range(miny, maxy + 1):
            print(puzzle.get((i, j), "."), end='')
        print("")


def rotR(facing):
    return facing[1], facing[0] * -1


def rotL(facing):
    return facing[1] * -1, facing[0]


def reverse(facing):
    return facing[0] * -1, facing[1] * -1


def traverse(puzzle, lx, ly):
    curr = (int(lx / 2), int(ly / 2))

    curr_facing = (-1, 0)

    infections = 0
    for _ in range(10000):
        node = puzzle.get(curr, ".")
        if node == '#':
            curr_facing = rotR(curr_facing)
            puzzle[curr] = '.'
        elif node == '.':
            curr_facing = rotL(curr_facing)
            puzzle[curr] = '#'
            infections += 1

        curr = tuple(map(sum, zip(curr, curr_facing)))

        #print_puzzle(puzzle)
    return infections


def traverse_part2(puzzle, lx, ly):
    curr = (int(lx / 2), int(ly / 2))

    curr_facing = (-1, 0)
    infections = 0
    for _ in range(10000000):
        node = puzzle.get(curr, ".")
        if node == '#':
            curr_facing = rotR(curr_facing)
            puzzle[curr] = 'F'
        elif node == '.':
            curr_facing = rotL(curr_facing)
            puzzle[curr] = 'W'
        elif node == 'W':
            infections += 1
            puzzle[curr] = '#'
        elif node == 'F':
            curr_facing = reverse(curr_facing)
            puzzle[curr] = '.'

        curr = tuple(map(sum, zip(curr, curr_facing)))

    return infections


if __name__ == '__main__':
    puzzle, lx, ly = read_puzzle('puzzles/22__.txt')
    infections = traverse_part2(puzzle, lx, ly)
    print(infections)
    