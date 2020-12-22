L = [line.strip() for line in open("input_22.txt").readlines()]

P = dict()
for line in L:
    if line.startswith("Pl"):
        player = int(line[7])
        P[player] = list()
    elif line:
        P[player].append(int(line))

while P[1] and P[2]:
    p1 = P[1].pop(0)
    p2 = P[2].pop(0)

    if p1 > p2:
        P[1].append(p1)
        P[1].append(p2)
    else:
        P[2].append(p2)
        P[2].append(p1)

print(max([sum([(len(P[p]) - i) * x for i, x in enumerate(P[p])]) for p in P]))
