L = open("input_03.txt").readlines()


def numtrees(right, down):
    x, y = 0, 0
    l = len(L[0]) - 1

    result = 0
    while y < len(L):
        if "#" == L[y][x % l]:
            result += 1
        x += right
        y += down
    return result


answer = (
    numtrees(1, 1) * numtrees(3, 1) * numtrees(5, 1) * numtrees(7, 1) * numtrees(1, 2)
)
print(f"Answer is: {answer}")
