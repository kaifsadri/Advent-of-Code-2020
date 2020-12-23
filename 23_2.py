INP = "496138527"
M = 1_000_000
L = [int(i) for i in INP] + list(range(10, M + 1))

CUPS = dict()
CUPS[L[0]] = (M, L[1])
CUPS[L[M - 1]] = (L[M - 2], L[0])
for i in range(1, M - 1):
    CUPS[L[i]] = (L[i - 1], L[i + 1])
CUR = L[0]


def nxt(C):
    global CUPS
    return CUPS[C][1]


def prv(C):
    global CUPS
    return CUPS[C][0]


def move():
    global CUPS, CUR
    picked = [nxt(CUR), nxt(nxt(CUR)), nxt(nxt(nxt(CUR)))]

    DES = CUR - 1 if CUR > 1 else M
    while DES in picked:
        DES -= 1
        if DES < 1:
            DES = M

    # now insert the picked cups:
    CUPS[CUR] = (prv(CUR), nxt(picked[2]))
    CUPS[picked[0]] = (DES, picked[1])
    CUPS[picked[2]] = (picked[1], nxt(DES))
    CUPS[DES] = (prv(DES), picked[0])
    CUR = nxt(CUR)


if __name__ == "__main__":
    for i in range(10_000_000):
        move()
    print(nxt(1) * nxt(nxt(1)))
