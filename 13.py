def read_firewall(name):
    firewall = {}
    with open(name, 'r') as f:
        for line in f:
            (layer, sz) = tuple(map(int, line.strip().split(": ")))
            #tuple: sz, security, packet, direction
            firewall[layer] = (sz, 0, True)
    return firewall


def update_securities(firewall):
    for l in firewall:
        dir = firewall[l][2]
        if firewall[l][1] + 1 == firewall[l][0]:
            dir = False
        elif not dir and firewall[l][1] == 0:
            dir = True

        f = lambda x, y: x + 1 if y else x - 1
        firewall[l] = (firewall[l][0], f(firewall[l][1], dir), dir)


def traversal(firewall, exit_if_caught=False):
    mv = -1
    caught = 0
    severity = 0
    for layer in range(max(firewall.keys()) + 1):
        mv += 1
        #print("Picosecond:", layer, firewall, caught, mv)

        if mv in firewall.keys():
            (sz, security, f) = firewall[mv]
            if security == 0:
                if exit_if_caught:
                    return 1, 0
                caught += 1
                severity += sz * layer

        update_securities(firewall)

    return caught, severity


def caught_or_not(firewall, delay=0):
    for pos_layer in range(max(firewall.keys()) + 1):
        sz = firewall.pop(pos_layer, (0, 0, 0))[0]
        multiples = (sz - 1) * 2
        #print(pos_layer, multiples, delay)
        if multiples > 0 and (delay + pos_layer) % multiples == 0:
            return True
    return False


def find_delay(fw):
    delay = 0
    while True:
        #delay 1 picosecond
        update_securities(fw)

        c, s = traversal(dict(fw), True)
        print("=========", c, delay)
        if c == 0:
            return delay + 1

        delay += 1


def find_optimized(fw):
    delay = 0
    while True:
        #delay 1 picosecond
        update_securities(fw)

        caught = caught_or_not(dict(fw), delay)
        print("=========", caught, delay)
        if not caught:
            return delay

        delay += 1


if __name__ == "__main__":
    firewall = read_firewall('13_puzzle.txt')
    #print(traversal(dict(firewall)))
    #print(find_delay(firewall))

    print(find_optimized(firewall))
