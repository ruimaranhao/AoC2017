def sum_(matrix, x, y):
    #print(".", matrix, x, y)
    s = 0
    if y > 0:
        s += matrix[x][y - 1]
    if y < len(matrix) - 1:
        s += matrix[x][y + 1]

    if x > 0:
        s += matrix[x - 1][y]
        if y > 0:
            s += matrix[x - 1][y - 1]
        if y < len(matrix) - 1:
            s += matrix[x - 1][y + 1]

    if x < len(matrix) - 1:
        s += matrix[x + 1][y]
        if y > 0:
            s += matrix[x + 1][y - 1]
        if y < len(matrix) - 1:
            s += matrix[x + 1][y + 1]

    return s


def day3_2(puzzle):
    matrix = [[1]]
    yield 1

    spirals = 0
    curr = 1
    el_side = 1
    while puzzle > curr:
        spirals += 1
        el_side += 2

        for x in matrix:
            x.insert(0, 0)
            x.append(0)
        matrix.insert(0, [0] * el_side)
        matrix.append([0] * el_side)

        hf = el_side // 2

        for p in range(hf + spirals, el_side):
            _hf = hf + spirals - 1

            matrix[_hf][p] = sum_(matrix, _hf, p)

            #left-hand side vertical
            for pp in range(_hf - 1, -1, -1):
                matrix[pp][len(matrix) - 1] = sum_(matrix, pp, len(matrix) - 1)
                curr = matrix[pp][len(matrix) - 1]
                yield matrix[pp][len(matrix) - 1]

            #top horizontal
            for pp in range(el_side - 1, -1, -1):
                matrix[0][pp] = sum_(matrix, 0, pp)
                curr = matrix[0][pp]
                yield matrix[0][pp]

            #right-hand side vertical
            for pp in range(1, len(matrix)):
                matrix[pp][0] = sum_(matrix, pp, 0)
                curr = matrix[pp][0]
                yield matrix[pp][0]

            #bottom horizontal
            for pp in range(0, el_side):
                matrix[len(matrix) - 1][pp] = sum_(matrix, len(matrix) - 1, pp)
                curr = matrix[len(matrix) - 1][pp]
                yield matrix[len(matrix) - 1][pp]

    yield curr

puzzle = 361527
for val in day3_2(puzzle):
    print(val)
    if val > puzzle:
        print("---> ",val)
        break
