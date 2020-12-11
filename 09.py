L = [int(i) for i in open("input_09.txt").readlines()]

preamble = 25

for item in range(preamble, len(L)):
    S = set(L[item - preamble : item])
    T = {i + j for i in S for j in S if i != j}
    if L[item] not in T:
        print(f"Answer for Part 1: {L[item]}")
        break

for index in range(0, item):
    end = 1
    while sum(L[index:end]) < L[item] and end < item:
        end += 1

    if L[item] == sum(L[index:end]):
        print(f"Answer for Part 2: {min(L[index:end])+max(L[index:end])}")
        break
