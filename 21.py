def read_rules(name):
    rules = {}
    with open(name, 'r') as f:
        for line in f:
            _line = line.strip().split(" => ")
            rules[_line[0]] = _line[1]
    return rules

def fractal(rules):
    art = ".#./..#/###"

    iters = 1
    i = 0
    while i < iters:
        art_ = ""
        if (len(art) - art.count("/")) % 3 == 0:
            for p in range(0, len(art), 3):
                print(p)
                out = rules[art[p, p + 4]]
                art_ = art_ + out



        i += 1


    print(art)


if __name__ == '__main__':
    rules = read_rules('21.txt')
    print(rules)
    fractal(rules)