L = [line.strip() for line in open("input_22.txt").readlines()]

P = dict()
for line in L:
    if line.startswith("Pl"):
        player = int(line[7])
        P[player] = list()
    elif line:
        P[player].append(int(line))


def play(One, Two):
    one = One.copy()
    two = Two.copy()
    Prev1 = set()
    Prev2 = set()
    while one and two:
        if tuple(one) in Prev1 or tuple(two) in Prev2:
            return 1
        else:
            Prev1.add(tuple(one))
            Prev2.add(tuple(two))
        p1 = one.pop(0)
        p2 = two.pop(0)
        if len(one) >= p1 and len(two) >= p2:
            winner = play(one[0:p1], two[0:p2])
        elif p1 > p2:
            winner = 1
        else:
            winner = 2
        if winner == 1:
            one.append(p1)
            one.append(p2)
        else:
            two.append(p2)
            two.append(p1)
    if one:
        return 1
    else:
        return 2


while P[1] and P[2]:
    p1 = P[1].pop(0)
    p2 = P[2].pop(0)
    Prev1 = set()
    Prev2 = set()
    if tuple(P[1]) in Prev1 or tuple(P[2]) in Prev2:
        break
    else:
        Prev1.add(tuple(P[1]))
        Prev2.add(tuple(P[2]))
    if len(P[1]) >= p1 and len(P[2]) >= p2:
        Winner = play(P[1][0:p1], P[2][0:p2])
    elif p1 > p2:
        Winner = 1
    else:
        Winner = 2
    if Winner == 1:
        P[1].append(p1)
        P[1].append(p2)
    elif Winner == 2:
        P[2].append(p2)
        P[2].append(p1)

print(max([sum([(len(P[p]) - i) * x for i, x in enumerate(P[p])]) for p in P]))
