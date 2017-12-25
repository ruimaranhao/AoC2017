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


if __name__ == "__main__":
    print(day2_1('puzzles/matrix.txt'))
    print(day2_2('puzzles/matrix.txt'))
