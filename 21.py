import numpy as np


def read_rules(name):
    rules = {}
    with open(name, 'r') as f:
        for line in f:
            _line = line.strip().split(" => ")
            rules[_line[0]] = np.matrix(list(map(list, _line[1].split("/"))))
    return rules


def fractal(rules):
    def mapping(a):
        possibilities = (a, np.flip(a, 0), np.flip(a, 1),
                         np.rot90(a, 1), np.rot90(a, 2), np.rot90(a, 3),
                         np.flip(np.rot90(a, 1), 0), np.flip(np.rot90(a, 2), 0), np.flip(np.rot90(a, 3), 0),
                         np.flip(np.rot90(a, 1), 1), np.flip(np.rot90(a, 2), 1), np.flip(np.rot90(a, 3), 1))
        for p in possibilities:
            as_str = "/".join(map(lambda l: "".join(l), p.tolist()))
            if as_str in rules:
                return rules[as_str]
        return None

    def compute(art, sz):
        __art = np.matrix([])
        for x in range(0, len(art), sz):
            __horiz = np.matrix([])
            for y in range(0, len(art), sz):
                sub = mapping(art[x:x + sz, y:y + sz])
                if len(__horiz) == 1:
                    __horiz = sub
                else:
                    __horiz = np.hstack((__horiz, sub))
            if len(__art) == 1:
                __art = __horiz
            else:
                __art = np.concatenate((__art, __horiz))
        return __art

    input = ".#./..#/###"
    art = np.matrix(list(map(list, input.split("/"))))

    iters = 18
    i = 0
    #print(art, np.count_nonzero(art == '#'), "\n")
    while i < iters:
        if len(art) % 2 == 0:
            __art = compute(art, 2)
        elif len(art) % 3 == 0:
            __art = compute(art, 3)

        art = __art
        i += 1

        #print(art, np.count_nonzero(art == '#'), "\n")
        print(i)

    return np.count_nonzero(art == '#')



if __name__ == '__main__':
    rules = read_rules('21puzzle.txt')
    numb = fractal(rules)
    print(numb)