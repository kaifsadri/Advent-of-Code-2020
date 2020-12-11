from collections import Counter

L = [0] + sorted([int(i) for i in open("input_10.txt").readlines()])
C = Counter({0: 1})
for item in L:
    C[item + 1] += C[item]
    C[item + 2] += C[item]
    C[item + 3] += C[item]

print(C[L[-1]])
