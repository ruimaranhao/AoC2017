
def spinlock(steps, times=2017):
    buffer = [0]
    curr_pos = 0

    back_to_1 = 0
    for val in range(1, times + 1):
        back_to_1 += 1
        curr_pos = (curr_pos + steps) % len(buffer) + 1
        buffer.insert(curr_pos, val)

    return buffer[curr_pos + 1]


def spinlock_on_the_fly(steps, times=2017):
    curr_pos = 0
    val_after_0 = 0
    for val in range(1, times + 1):
        curr_pos = (curr_pos + steps) % val + 1
        if curr_pos == 1:
            val_after_0 = val
    return val_after_0


if __name__ == "__main__":
    print(spinlock(349))
    print(spinlock_on_the_fly(349, 50000000))
