
def read_tap(name):
    l = []
    with open(name, 'r') as f:
        for line in f:
            l.append(int(line.strip()))
    return l


def steps(matrix):
    pos = 0
    x_len = len(matrix)

    step = 0
    while pos < x_len:
        _pos = pos
        if matrix[pos] + _pos > x_len:
            return step
        pos = matrix[pos] + _pos
        matrix[_pos] += 1
        step += 1

    return step


def steps_decrease3(matrix):
    pos = 0
    x_len = len(matrix)

    step = 0
    while pos < x_len:
        _pos = pos
        if matrix[pos] + _pos > x_len:
            return step

        pos = matrix[pos] + _pos

        if matrix[_pos] >= 3:
            matrix[_pos] -= 1
        else:
            matrix[_pos] += 1
        step += 1

    return step


if __name__ == "__main__":
    m = read_tap('5.txt')
    s = steps_decrease3(m)
    print(s)
