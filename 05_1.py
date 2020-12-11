L = [i.strip() for i in open("input_05.txt").readlines()]
S = 0
G = {"F": 0, "B": 1, "R": 1, "L": 0}


highest = 0
for line in L:
    I = list(map(lambda x: G[x], line))
    Id = sum([I[i] * 2 ** (9 - i) for i in range(0, 10)])
    if Id > highest:
        highest = Id

print(highest)
