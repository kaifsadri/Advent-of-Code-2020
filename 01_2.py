L = sorted([int(i) for i in open("input_01.txt").readlines()])
S = set(L)

right = 0
left = len(L) - 1
found = False
while found is False:
    if 2020 <= (L[right] + L[right] + L[left]):
        left -= 1
        continue
    else:
        if int(2020 - L[left] - L[right]) in S:
            print(f"Answer is: {L[right]*L[left]*(2020-L[left]-L[right])}")
            found = True
        else:
            right += 1
            continue
