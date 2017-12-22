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


def print_puzzle(puzzle, lx, ly):
    for i in range(lx):
        for j in range(ly):
            print(puzzle[(i,j)], end='')
        print("")


def traverse(puzzle, lx, ly):
    curr = (int(lx / 2), int(ly / 2))

    print(puzzle)
    for _ in range(2):
        print("----")
        node = puzzle[curr]
        if node == '#':
            puzzle[curr] = '.'
            curr = (curr[0] + 1, curr[1])
        elif node == '.':
            puzzle[curr] = '#'
            curr = (curr[0], curr[1] - 1)

            print_puzzle(puzzle, lx, ly)


if __name__ == '__main__':
    puzzle, lx, ly = read_puzzle('22.txt')
    traverse(puzzle, lx, ly)
