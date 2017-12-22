def read_lst(name):
    with open(name, 'r') as f:
        lst = f.readline().strip().split(",")
    return list(map(int, lst))


def rev_list(lst, index, length):
    rev = lst[:]
    for i in range(length):
        rev[(index + i) % len(lst)] = lst[(index + length - i - 1) % len(lst)]
    return rev


def twist(inps, lst=list(range(256)), index=0, skip=0):
    for length in inps:
        lst = rev_list(lst, index, length)
        index = (index + length + skip) % len(lst)
        skip += 1
    return lst, index, skip


def hash(inps, iters=64):
    inps = list(map(ord, inps)) + [17, 31, 73, 47, 23]

    lst, index, skip = twist(inps)

    for _ in range(iters-1):
        lst, index, skip = twist(inps, lst, index, skip)

    final = ""
    for i in range(16):
        sub = lst[i * 16:(i + 1) * 16]

        h = sub[0]
        for c in sub[1:]:
            h = h ^ c
        final += "{:02x}".format(h)

    return final


if __name__ == "__main__":
    inps = read_lst('10.txt')

    ##
    ## Part 1
    ##
    (lst, idx, skip) = twist(inps)
    print(lst[0] * lst[1])


    ##
    ## Part 2
    ##
    print(hash(",".join(map(str, inps))))

