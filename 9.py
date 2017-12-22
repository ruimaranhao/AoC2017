def read_instr(name):
    lines = []
    with open(name, 'r') as f:
        lines = f.readlines()
    return list(map(lambda l: l.strip(), lines))


def score(stream):
    stack = []

    ignore = False
    groups = 0
    lst = 0
    comment = False
    nChrs = 0
    for c in stream:
        if ignore:
            ignore = False
            continue
        if c == '!':
            ignore = True
            continue

        if comment:
            nChrs += 1

        if c == '<':
            comment = True
        elif c == '>':
            nChrs -= 1
            comment = False
        elif not comment and c == '{' or c == '[':
            lst += 1
            stack.append(lst)
        elif not comment and c == '!':
            ignore = True
        elif not comment and c == '}':
            _c = stack.pop()
            groups += _c
            lst = stack[-1] if len(stack) > 0 else 0
        elif not comment and c == ']':
            _c = stack.pop()

    if len(stack) != 0:
        print("FAILURE")
    return groups, nChrs


if __name__ == "__main__":
    instrs = read_instr('9.txt')

    for ins in range(len(instrs)):
        print(ins + 1, score(instrs[ins]))
