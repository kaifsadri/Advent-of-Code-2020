L = [i.strip() for i in open("input_05.txt").readlines()]
S = 0
G = {"F": 0, "B": 1, "R": 1, "L": 0}


Plane = set()
for line in L:
    I = list(map(lambda x: G[x], line))
    Plane.add(sum([I[i] * 2 ** (9 - i) for i in range(0, 10)]))


for seat in range(min(Plane) + 1, max(Plane)):
    if seat not in Plane and seat + 1 in Plane and seat - 1 in Plane:
        print(seat)
