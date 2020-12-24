M = 1_000_000
INP = "496138527"
L = [int(i) for i in INP] + list(range(10, M + 1))

CUPS = dict()
for i, _ in enumerate(L[:-1]):
    CUPS[_] = L[i + 1]
CUPS[M] = L[0]
CUR = L[0]


def move():
    global CUPS, CUR
    picked = [CUPS[CUR], CUPS[CUPS[CUR]], CUPS[CUPS[CUPS[CUR]]]]

    DES = CUR - 1 if CUR > 1 else M
    while DES in picked:
        DES -= 1
        if DES < 1:
            DES = M

    # now insert the picked cups:
    CUPS[CUR] = CUPS[picked[2]]
    CUPS[picked[2]] = CUPS[DES]
    CUPS[DES] = picked[0]
    CUR = CUPS[CUR]


if __name__ == "__main__":
    for i in range(10_000_000):
        move()
    print(CUPS[1] * CUPS[CUPS[1]])
