from day10 import hash


def n_squares(inp, rep=128):
    used = 0
    for i in range(rep):
        H = knot(inp + "-" + str(i))
        hash_int = bin(int(H, 16))[2:].zfill(128)
        used += sum(map(int, hash_int))

    return used


def dfs_adj(graph, program=(0,0)):
    stack = [program]

    visited = set()
    while len(stack) != 0:
        curr = stack.pop()

        if curr in visited:
            continue

        visited.add(curr)

        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        func = lambda m: tuple(map(sum, zip(curr, m)))
        to_visit = list(map(func, moves))
        for (x, y) in to_visit:
            if 0 <= x < 128 and 0 <= y < 128 and graph[x][y] == 1:
                stack.append((x, y))

    return len(visited), visited


def asMatrix(inp, rep=128):
    matrix = []
    for i in range(rep):
        H = hash(inp + "-" + str(i))
        hash_int = bin(int(H, 16))[2:].zfill(128)
        matrix.append(list(map(int, hash_int)))

    return matrix


def countRegions(matrix):
    seen = set()
    groups = 0
    for p1 in range(128):
        for p2 in range(128):
            if matrix[p1][p2]:
                (sz, grp) = dfs_adj(matrix, (p1, p2))
                #print((p1, p2), sz, grp)

                if len(seen.intersection(grp)) == 0:
                    groups += 1

                seen = seen.union(grp)

    return groups


if __name__ == "__main__":
    inp = "wenycdww"
    #inp = "flqrgnkx"
    print(countRegions(asMatrix(inp)))
