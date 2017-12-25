def day2_1(matrix):
    checksum = 0
    with open(matrix, 'r') as f:
        for line in f:
            arr = list(map(int, line.strip().split("\t")))
            _max = max(arr)
            _min = min(arr)
            checksum += (_max - _min)
    return checksum


def day2_2(matrix):
    checksum = 0
    with open(matrix, 'r') as f:
        for line in f:
            arr = list(map(int, line.strip().split("\t")))
            for i in range(len(arr) - 1):
                for ii in range(i + 1, len(arr)):
                    if arr[i] % arr[ii] == 0:
                        checksum += int(arr[i] / arr[ii])
                        continue
                    elif arr[ii] % arr[i] == 0:
                        checksum += int(arr[ii] / arr[i])
                        continue
    return checksum


def bit_division(a, b):
    def bit_add(x, y):
        while y != 0:
            carry = x & y
            x = x ^ y
            y = carry << 1
        return x

    def bit_sub(x, y):
        while y != 0:
            borrow = (~x) & y
            x = x ^ y
            y = borrow << 1
        return x

    quo = 0
    while a >= b:
        a = bit_sub(a, b)
        quo = bit_add(quo, 1)

    return quo, a


def day2_2bit(matrix):
    checksum = 0
    with open(matrix, 'r') as f:
        for line in f:
            arr = list(map(int, line.strip().split("\t")))
            for i in range(len(arr) - 1):
                for ii in range(i + 1, len(arr)):
                    _, rem1 = bit_division(arr[i], arr[ii])
                    _, rem2 = bit_division(arr[ii], arr[i])
                    if rem1 == 0:
                        checksum += int(arr[i] / arr[ii])
                        continue
                    elif rem2 == 0:
                        checksum += int(arr[ii] / arr[i])
                        continue
    return checksum



if __name__ == "__main__":
    #print(day2_1('puzzles/matrix.txt'))
    print(day2_2('puzzles/matrix.txt'))

    print(day2_2bit('puzzles/matrix.txt'))

