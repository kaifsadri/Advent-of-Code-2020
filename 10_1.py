L = sorted([int(i) for i in open("input_10.txt").readlines()])

threes = 0
ones = 0
for index in range(len(L) - 1):
    if 1 == L[index + 1] - L[index]:
        ones += 1
    elif 3 == L[index + 1] - L[index]:
        threes += 1
    elif 3 < L[index + 1] - L[index]:
        print(f"ERROR: {index}")

print((ones + 1) * (threes + 1))
