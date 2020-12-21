from collections import defaultdict
from functools import reduce

L = [line.strip() for line in open("input_21.txt").readlines()]

S = defaultdict(lambda: list())
ING = set()

for line in L:
    ing, alg = line.split(" (contains ")
    alg = alg[:-1].split(", ")
    ing = ing.split(" ")
    ING = ING.union(set(ing))
    for allergene in alg:
        S[allergene].append(ing)

for alg in S:
    S[alg] = list(reduce(set.intersection, [set(i) for i in S[alg]]))

T = dict()
finished = False
while S.values():
    finished = True
    s = S.copy()
    for alg in S:
        if len(S[alg]) == 1:
            T[S[alg][0]] = alg
            s.pop(alg)
            finished = False
        else:
            for item in S[alg]:
                if item in T:
                    S[alg].remove(item)
    S = s

ING = ING - set(T.keys())
C = 0
for line in L:
    for item in line.split(" "):
        if item in ING:
            C += 1

print(C)
