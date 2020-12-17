L = ["#.......", ".#..#..#", "....#.#.", ".##..#.#", "#######.", "#...####", "###.##..", ".##.#.#."]

ACTIVES = set()
for y, _ in enumerate(L):
    for x, ch in enumerate(L[y]):
        if ch == "#":
            ACTIVES.add((x, y, 0))


def activeneighbors(x, y, z):
    global ACTIVES
    count = 0
    r = [-1, 0, 1]
    for i in r:
        for j in r:
            for k in r:
                if (i, j, k) != (0, 0, 0) and (x + i, y + j, z + k) in ACTIVES:
                    count += 1
    return count


for i in range(6):
    A = set()
    X = [min([point[0] for point in ACTIVES]), max([point[0] for point in ACTIVES])]
    Y = [min([point[1] for point in ACTIVES]), max([point[1] for point in ACTIVES])]
    Z = [min([point[2] for point in ACTIVES]), max([point[2] for point in ACTIVES])]
    for x in range(X[0] - 1, X[1] + 2):
        for y in range(Y[0] - 1, Y[1] + 2):
            for z in range(Z[0] - 1, Z[1] + 2):
                if (x, y, z) in ACTIVES and activeneighbors(x, y, z) in {2, 3}:
                    A.add((x, y, z))
                if (x, y, z) not in ACTIVES and activeneighbors(x, y, z) == 3:
                    A.add((x, y, z))
    ACTIVES = A

print(len(ACTIVES))