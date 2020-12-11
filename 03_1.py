L = open("input_03.txt").readlines()


right = 3
down = 1
x, y = 0, 0
l = len(L[0]) - 1

result = 0
while y < len(L):
    if "#" == L[y][x % l]:
        result += 1
    x += right
    y += down

print(f"Answer is: {result}")