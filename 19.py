import string


def read_puzzle(name):
    puzzle = {}
    with open(name, 'r') as f:
        for row, line in enumerate(f):
            for col, char in enumerate(line):
                if not (char == ' ' or char == '\n'):
                    puzzle[row, col] = char
    return puzzle


def traversal(puzzle):
    def init():
        return [(0, col) for row, col in puzzle if row == 0 and puzzle[0, col] == '|'][0]

    x, y = init()
    collected = []

    step = (1, 0)
    step_count = 0
    while True:
        step_count += 1
        (x, y) = (x + step[0], y + step[1])

        if (x, y) not in puzzle:
            break

        if puzzle[x, y] in string.ascii_uppercase:
            collected.append(puzzle[x, y])
        elif puzzle[x, y] == '+':
            if (x + step[1], y + step[0]) in puzzle:
                step = (step[1], step[0])
            elif (x - step[1], y - step[0]) in puzzle:
                step = (-step[1], -step[0])

    return collected, step_count


if __name__ == '__main__':
    puzzle = read_puzzle('19.txt')
    (c, count) = traversal(puzzle)
    print("".join(c))
    print(count)

