def read(name):
    with open(name, 'r') as f:
        instr = f.readline().strip().split(",")
    return instr


def spin(lst, n):
    lst[:len(lst) - n], lst[len(lst)-n:] = lst[len(lst) - n:], lst[:len(lst) - n]


def exchange(lst, a, b):
    lst[a], lst[b] = lst[b], lst[a]


def partner(lst, a, b):
    exchange(lst, lst.index(a), lst.index(b))


def dance(lst, instr):
    for i in instr:
        if i[0] == 's':
            val = int(i[1:])
            spin(lst, val)
        elif i[0] == 'x':
            arr = i[1:].split("/")
            exchange(lst, int(arr[0]), int(arr[1]))
        elif i[0] == 'p':
            arr = i[1:].split("/")
            partner(lst, arr[0], arr[1])
    return "".join(progs)


if __name__ == "__main__":
    #progs = list("abcde")
    #f = ['s1', 'x3/4', 'pe/b']
    progs = list("abcdefghijklmnop")
    instrs = read('15.txt')

    times = 1_000_000_000

    memory = ["".join(progs)]
    as_str = dance(progs, instrs)
    print("Parte1:", as_str)
    while True:
        if as_str in memory:
            print("Parte2:", memory[times % len(memory)])
            break
        memory.append(as_str)

        dance(progs, instrs)
        as_str = "".join(progs)

