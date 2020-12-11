from functools import reduce

L = [i.strip() for i in open("input_06.txt").readlines()] + [""]

S = 0
A = [set()]
for line in L:
    if line:
        for c in line:
            A[-1].add(c)
        A.append(set())
    else:
        print(reduce(set.intersection, [a for a in A[:-1]]))
        S += len(reduce(set.intersection, [a for a in A[:-1]]))
        A = [set()]

print(S)
