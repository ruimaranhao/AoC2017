
def read_tower(name):
    tower = {}
    with open(name, 'r') as f:
        lines = list(map(lambda s: s.strip(), f.readlines()))
        for line in lines:
            if "->" in line:
                k_v = line.split("->")

                t = k_v[0].split()
                key = t[0]

                v = k_v[1].split(",")
                v = list(map(lambda s: s.strip(), v))
                tower[key] = (eval(t[1]), v)
            else:
                t = line.split()
                key = t[0]
                tower[key] = (eval(t[1]), None)
    return tower


def find_base(tower):
    ktower = list(tower.keys())
    for w, i in tower.values():
        if i:
            for el in i:
                ktower
                ktower.remove(el)

    return ktower[0] if len(ktower) == 1 else None


def weights(tower):
    def compute_w(b):
        _w = tower[b][0]
        if tower[b][1]:
            for t in tower[b][1]:
                _w += compute_w(t)
        return _w

    def depth_first(b, level=0):
        #print("\t" * level, tower[b])

        if not tower[b][1]:
            return tower[b][0]

        children = []
        for p in tower[b][1]:
            v = depth_first(p, level + 1)
            if v:
                children.append(depth_first(p, level + 1))
            else:
                return None

        #print("\t" * level, b, children, sum(children))
        if len(set(children)) != 1:
            print("WARNING: ", children, tower[b])

            if children.count(max(children)) == 1:
                val = max(children)
            else:
                val = min(children)

            idx = children.index(val)
            disc = tower[b][1][idx]
            print(tower[disc][0] - (max(children) - min(children)))
            return None

        return sum(children) + tower[b][0]

    base = find_base(tower)
    programs = tower[base][1]
    punb = {}
    for p in programs:
        punb[p] = compute_w(p)

    maximum = max(punb, key=punb.get)

    depth_first(maximum)

    return punb[maximum]

if __name__ == "__main__":
    tower = read_tower('tower.txt')
    print(find_base(tower))
    print(weights(tower))

