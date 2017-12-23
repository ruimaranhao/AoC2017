import math

def read(name):
    with open(name, 'r') as f:
        instr = list(map(lambda line: line.strip().split(" "), f.readlines()))
    return instr


def get(value, d):
    if value.isdigit():
        return int(value)
    elif value[1:].isdigit():
        return int(value)

    return d.get(value, 0)


def execute(instructions):
    registers = {chr(k): 0 for k in range(ord('a'), ord('n') + 1)}

    i = 0
    muls = 0
    while 0 <= i < len(instructions):
        instr = instructions[i]
        op, reg, val = instr[0], instr[1], instr[2]
        if op == 'set':
            registers[reg] = get(val, registers)
        elif op == 'sub':
            registers[reg] -= get(val, registers)
        elif op == 'mul':
            muls += 1
            registers[reg] *= get(val, registers)
        elif op == 'jnz':
            if get(reg, registers) != 0:
                i += get(val, registers)
                continue
        i += 1

    return muls


def is_prime(n):
    """"pre-condition: n is a nonnegative integer
    post-condition: return True if n is prime and False otherwise."""
    if n < 2:
         return False;
    if n % 2 == 0:
         return n == 2  # return False
    k = 3
    while k*k <= n:
         if n % k == 0:
             return False
         k += 2
    return True


def execute_part2(instructions):
    registers = {chr(k): 0 for k in range(ord('a'), ord('n') + 1)}
    registers['a'] = 1

    i = 0
    muls = 0
    while i < 11:
        instr = instructions[i]
        op, reg, val = instr[0], instr[1], instr[2]
        if op == 'set':
            registers[reg] = get(val, registers)
        elif op == 'sub':
            registers[reg] -= get(val, registers)
        elif op == 'mul':
            muls += 1
            registers[reg] *= get(val, registers)
        elif op == 'jnz':
            if get(reg, registers) != 0:
                i += get(val, registers)
                continue
        i += 1

    #registers['b'] = 107900
    #registers['c'] = 124900

    registers['h'] = 0
    for b in range(registers['b'], registers['c'] + 1, 17):
        for d in range(2, int(math.sqrt(b))):
            if b % d == 0:
                registers['h'] += 1
                break
    return registers['h']


def execute_part2_optz():
    h = 0
    for b in range(107900, 124901, 17):
        for d in range(2, int(math.sqrt(b))):
            if b % d == 0:
                h += 1
                break
    return h


if __name__ == "__main__":
    instrs = read('puzzles/23.txt')
    #print(execute(instrs))
    print(execute_part2_optz())


