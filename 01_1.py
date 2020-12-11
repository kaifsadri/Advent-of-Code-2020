L = sorted([int(i) for i in open("input_01.txt").readlines()])
right = 0
left = len(L) - 1
while True:
    if right > left:
        print("Not found")
        break
    elif 2020 < (L[right] + L[left]):
        left -= 1
        continue
    elif 2020 > (L[right] + L[left]):
        right += 1
        continue
    elif 2020 == (L[right] + L[left]):
        print("Answer is: ", L[right] * L[left])
        break
