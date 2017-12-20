def read_particles(name):
    particles = {}
    with open(name, 'r') as f:
        n = 0
        for line in f:
            data = line.strip().split(", ")
            pos = data[0]
            v = data[1]
            a = data[2]
            pvals = tuple(map(int, pos[3:-1].split(",")))
            pvelo = tuple(map(int, v[3:-1].split(",")))
            pacel = tuple(map(int, a[3:-1].split(",")))
            particles[n] = [pvals, pvelo, pacel, sum(pvals)]
            n += 1

    return particles


def tick(particles):
    new = {}
    for pa in particles:
        vals = particles[pa]
        p = vals[0]
        v = vals[1]
        a = vals[2]
        v = (v[0] + a[0], v[1] + a[1], v[2] + a[2])
        p = (p[0] + v[0], p[1] + v[1], p[2] + v[2])
        man = sum(map(abs, p))
        new[pa] = [p, v, a, man]
    return new


def part1(particles):
    last = []

    iters = 0
    while True:
        particles = tick(particles)

        p_ = 0
        p_dist = abs(particles[0][3])
        for p in particles:
            if p_dist > abs(particles[p][3]):
                p_ = p
                p_dist = abs(particles[p][3])

        last.append(p_)
        if len(last) == 200 and len(set(last)) == 1:
            print("Particle:", p_, p_dist)
            return p_, iters
        elif len(last) == 200:
            last.pop(0)

        iters += 1


def part2(particles, iters):
    n = 0
    while n < iters:
        particles = tick(particles)
        part = {}
        for p in particles:
            count = 0
            for p1 in particles:
                if particles[p][0] == particles[p1][0]:
                    count += 1
            if count == 1:
                part[p] = particles[p]

        particles = part
        n += 1

    return len(particles)


if __name__ == '__main__':
    particles = read_particles('20.txt')
    print(len(particles), particles)
    (_, iters) = part1(particles)
    print(part2(particles, iters))
