
def find_index_max(banks):
    max = 0
    idx = 0
    for i in range(len(banks)):
        if max < banks[i]:
            max = banks[i]
            idx = i
    return idx


def redistribute(banks):
    idx = find_index_max(banks)
    n_banks = banks[idx]
    banks[idx] = 0

    idx = (idx + 1) % len(banks)
    while n_banks > 0:
        banks[idx] += 1
        idx = (idx + 1) % len(banks)
        n_banks -= 1

    return banks


def how_many(banks):
    cycle = {}
    memory = set()
    count = 0

    as_str = ''
    while as_str not in memory:
        memory.add(as_str)
        cycle[as_str] = count
        count += 1
        banks = redistribute(banks)
        as_str = ''.join(str(e) for e in banks)

    return count, cycle[as_str]


if __name__ == "__main__":
    puzzle = "14	0	15	12	11	11	3	5	1	6	8	4	9	1	8	4"
    l_puzzle = list(map(int, puzzle.split("\t")))
    (s, cycles) = how_many(l_puzzle)
    #(s, cycles) = how_many([0, 2, 7, 0])
    print(s - cycles)

