import re


def read_instr(name):
    instr = {}
    with open(name, 'r') as f:
        state = f.readline().strip().split(" ")[-1][0]
        steps = int(re.findall(r'\d+', f.readline())[0])

        while f.readline():
            _s = f.readline().strip()[-2]
            _c = int(f.readline().strip()[-2])
            _w = int(f.readline().strip()[-2])
            _u = f.readline().strip()
            if _u.endswith("right."):
                _u = 1
            else:
                _u = -1
            _n = f.readline().strip()[-2]

            __c = int(f.readline().strip()[-2])
            __w = int(f.readline().strip()[-2])
            __u = f.readline().strip()
            if __u.endswith("right."):
                __u = 1
            else:
                __u = -1
            __n = f.readline().strip()[-2]

            instr.update({_s: {_c: (_w, _u, _n), __c: (__w, __u, __n)}})

    return state, steps, instr


def run(steps, state, instructions):
    tape = [0]

    pos = 0
    for _ in range(steps):
        state_instr = instructions[state]
        val = tape[pos]
        tape[pos] = state_instr[val][0]
        pos += state_instr[val][1]

        if pos < 0:
            tape.insert(0, 0)
            pos = 0
        elif pos >= len(tape):
            tape.append(0)
            pos = len(tape) - 1
        state = state_instr[val][2]

    return sum(tape)


if __name__ == "__main__":
    state, steps, instructions = read_instr("puzzles/25_puzzle.txt")

    #steps = 6
    #instructions = {'A': {0: (1, 1, 'B'), 1: (0, -1, 'B')},
    #                'B': {0: (1, -1, 'A'), 1: (1, 1, 'A')}}

    print(run(steps, state, instructions))

