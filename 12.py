def graph(name):
    g = {}
    with open(name, 'r') as f:
        for line in f:
            _line = line.strip().split(" <-> ")
            p = int(_line[0])
            conn = list(map(int, _line[1].split(", ")))
            g[p] = conn
    return g


def dfs(graph, program):
    stack = [program]

    visited = set()
    while len(stack) != 0:
        curr = stack.pop()

        if curr in visited:
            continue

        visited.add(curr)
        for p in graph[curr]:
            stack.append(p)

    return len(visited), visited


def how_many_groups(graph):

    seen = set()

    groups = 0
    for p in graph.keys():
        (sz, grp) = dfs(graph, p)

        if len(seen.intersection(grp)) == 0:
            groups += 1

        seen = seen.union(grp)

    return groups


if __name__ == '__main__':
    graph = graph('12_puzzle.txt')
    print(how_many_groups(graph))
