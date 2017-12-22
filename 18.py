from collections import deque


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


def play(instructions):
    vals = {}
    ins_pos = 0
    last = 0
    while ins_pos <= len(instructions):
        instr = instructions[ins_pos]
        if instr[0] == 'set':
            vals[instr[1]] = get(instr[2], vals)
        elif instr[0] == 'add':
            vals[instr[1]] = get(instr[1], vals) + get(instr[2], vals)
        elif instr[0] == 'mul':
            vals[instr[1]] = get(instr[1], vals) * get(instr[2], vals)
        elif instr[0] == 'mod':
            vals[instr[1]] = get(instr[1], vals) % get(instr[2], vals)
        elif instr[0] == 'snd':
            last = get(instr[1], vals)
        elif instr[0] == 'rcv':
            if get(instr[1], vals) > 0:
                print("RCV", last)
                break
        elif instr[0] == 'jgz':
            if get(instr[1], vals) > 0:
                ins_pos += get(instr[2], vals) - 1

        ins_pos += 1


def decode_instr(instructions, vals, queue_in, queue_out):
    while (vals['counter']>=0) and (vals['counter'] < len(instructions)):
        instr = instructions[vals['counter']]
        if instr[0] == 'set':
            vals[instr[1]] = get(instr[2], vals)
        elif instr[0] == 'add':
            vals[instr[1]] = get(instr[1], vals) + get(instr[2], vals)
        elif instr[0] == 'mul':
            vals[instr[1]] = get(instr[1], vals) * get(instr[2], vals)
        elif instr[0] == 'mod':
            vals[instr[1]] = get(instr[1], vals) % get(instr[2], vals)
        elif instr[0] == 'snd':
            queue_out.append(get(instr[1], vals))
            vals['__sends'] = vals['__sends'] + 1
        elif instr[0] == 'rcv':
            if len(queue_in) == 0:
                return True
            vals[instr[1]] = queue_in.popleft()
        elif instr[0] == 'jgz':
            if get(instr[1], vals) > 0:
                vals["counter"] += get(instr[2], vals) - 1
        vals['counter'] += 1

    return False


def play_duet(instructions):
    vals_p0 = {'p': 0, 'counter': 0, '__sends': 0}
    vals_p1 = {'p': 1, 'counter': 0, '__sends': 0}

    forA = deque()
    forB = deque()
    while True:
        decode_instr(instructions, vals_p0, forA, forB)
        decode_instr(instructions, vals_p1, forB, forA)
        if len(forA) == 0 and len(forA) == 0:
            break

    print(vals_p1['__sends'])


if __name__ == "__main__":
    instructions = read('18.txt')
    #play(instructions)
    play_duet(instructions)
