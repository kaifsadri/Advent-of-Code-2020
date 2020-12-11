L = [i.strip() for i in open("input_06.txt").readlines()] + [""]
S = 0
G = dict()
for line in L:
    if line:
        for c in line:
            G[c] = 1
    else:
        S += len(G)
        G = dict()

print(S)
