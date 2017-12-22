def read_instr(name):
    lines = []
    with open(name, 'r') as f:
        lines = f.readlines()
    return list(map(lambda l: l.strip(), lines))

def decode_ins(ins):
    if ' dec ' in ins:
        s = ' dec '
        f = lambda x, y: x - y
    elif ' inc ' in ins:
        s = ' inc '
        f = lambda x, y: x + y
    parts = ins.split(s)
    return(f, parts[0], parts[1])


def decode_cond(cond, values):
    expr = cond.split(" ")
    expr[0] = str(values.get(expr[0], 0))
    return eval("".join(expr))


def decode(instrs):
    values = {}

    max_value = 0
    for i in instrs:
        spl = i.split(" if ")
        if decode_cond(spl[1], values):
            triple_instr = decode_ins(spl[0])
            res = triple_instr[0](values.pop(triple_instr[1], 0), int(triple_instr[2]))
            max_value = res if max_value < res else max_value
            values[triple_instr[1]] = res

    return (values[max(values, key=lambda key: values[key])], max_value)



if __name__ == "__main__":
    instrs = read_instr('8_puzzle.txt')
    print(decode(instrs))
