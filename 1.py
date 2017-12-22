def day1_1(seq):
    count = 0
    for i in range(len(seq)):
        if seq[i] == seq[(i + 1) % len(seq)]:
            count += seq[i]
    return count


def day1_2(seq):
    ahead = int(len(seq) / 2)

    count = 0
    for i in range(len(seq)):
        if seq[i] == seq[(i + ahead) % len(seq)]:
            count += seq[i]

    if seq[ahead] == seq[-1]:
        count += seq[-1]

    return count

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
            print(line)
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


def day3(puzzle):
    spirals = 0
    curr = 1
    el_side = 1
    while puzzle > curr:
        spirals += 1
        curr += (spirals * 8)
        el_side += 2

    curr_el_side = el_side
    side = 1
    while curr != puzzle:
        curr -= 1
        curr_el_side -= 1
        if curr_el_side == 0:
            curr += 1
            curr_el_side = el_side
            side += 1

    if side == 1 or side == 3:
        #horizontal
        _vertical = el_side // 2
        _horizontal = abs(curr_el_side - 1 - (el_side // 2))
        print("manh_h", _vertical + _horizontal)

    else:
        #vertical
        _horizontal = el_side // 2
        _vertical = abs(curr_el_side - 1 - (el_side // 2))
        print("manh_v", _vertical + _horizontal)

    return _vertical + _horizontal


def sum_(matrix, x, y):
    #print(".", matrix, x, y)
    s = 0
    if y > 0:
        s += matrix[x][y - 1]
    if y < len(matrix) - 1:
        s += matrix[x][y + 1]

    if x > 0:
        s += matrix[x - 1][y]
        if y > 0:
            s += matrix[x - 1][y - 1]
        if y < len(matrix) - 1:
            s += matrix[x - 1][y + 1]

    if x < len(matrix) - 1:
        s += matrix[x + 1][y]
        if y > 0:
            s += matrix[x + 1][y - 1]
        if y < len(matrix) - 1:
            s += matrix[x + 1][y + 1]

    return s


def day3_2(puzzle):
    matrix = [[1]]
    yield 1

    spirals = 0
    curr = 1
    el_side = 1
    while puzzle > curr:
        spirals += 1
        curr += (spirals * 8)
        el_side += 2

        for x in matrix:
            x.insert(0, 0)
            x.append(0)
        matrix.insert(0, [0] * el_side)
        matrix.append([0] * el_side)

        hf = el_side // 2

        for p in range(hf + spirals, el_side):
            _hf = hf + spirals - 1

            matrix[_hf][p] = sum_(matrix, _hf, p)

            #left-hand side vertical
            for pp in range(_hf - 1, -1, -1):
                matrix[pp][len(matrix) - 1] = sum_(matrix, pp, len(matrix) - 1)

                yield matrix[pp][len(matrix) - 1]

            #top horizontal
            for pp in range(el_side - 1, -1, -1):
                matrix[0][pp] = sum_(matrix, 0, pp)

                yield matrix[0][pp]

            #right-hand side vertical
            for pp in range(1, len(matrix)):
                matrix[pp][0] = sum_(matrix, pp, 0)

                yield matrix[pp][0]

            #bottom horizontal
            for pp in range(0, el_side):
                matrix[len(matrix) - 1][pp] = sum_(matrix, len(matrix) - 1, pp)

                yield matrix[len(matrix) - 1][pp]

    yield curr


if __name__ == "__main__":
    #c = day1_1(list(map(int, list("91212129"))))
    #c = day1_1(list(map(int, list("3294199471327195994824832197564859876682638188889768298894243832665654681412886862234525991553276578641265589959178414218389329361496673991614673626344552179413995562266818138372393213966143124914469397692587251112663217862879233226763533911128893354536353213847122251463857894159819828724827969576432191847787772732881266875469721189331882228146576832921314638221317393256471998598117289632684663355273845983933845721713497811766995367795857965222183668765517454263354111134841334631345111596131682726196574763165187889337599583345634413436165539744188866156771585647718555182529936669683581662398618765391487164715724849894563314426959348119286955144439452731762666568741612153254469131724137699832984728937865956711925592628456617133695259554548719328229938621332325125972547181236812263887375866231118312954369432937359357266467383318326239572877314765121844831126178173988799765218913178825966268816476559792947359956859989228917136267178571776316345292573489873792149646548747995389669692188457724414468727192819919448275922166321158141365237545222633688372891451842434458527698774342111482498999383831492577615154591278719656798277377363284379468757998373193231795767644654155432692988651312845433511879457921638934877557575241394363721667237778962455961493559848522582413748218971212486373232795878362964873855994697149692824917183375545192119453587398199912564474614219929345185468661129966379693813498542474732198176496694746111576925715493967296487258237854152382365579876894391815759815373319159213475555251488754279888245492373595471189191353244684697662848376529881512529221627313527441221459672786923145165989611223372241149929436247374818467481641931872972582295425936998535194423916544367799522276914445231582272368388831834437562752119325286474352863554693373718848649568451797751926315617575295381964426843625282819524747119726872193569785611959896776143539915299968276374712996485367853494734376257511273443736433464496287219615697341973131715166768916149828396454638596713572963686159214116763"))))
    #c = da1y(list(map(int, list("12131415"))))
    #print(c)

    #print(day2('matrix.txt'))
    #print(day2_2('matrix.txt'))

    #day3(1)
    #day3(12)
    #day3(23)
    #day3(1024)
    #day3(361527)
    #day3(277678)

    #print(day3_2(361527))
    #print(day3_2(277678))

    puzzle = 361527
    for i in day3_2(puzzle):
        print(i)
        print("")
        if i > puzzle:
            print("---> ", i)
            break

