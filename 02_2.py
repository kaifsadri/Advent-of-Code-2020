L = open("input_02.txt").readlines()


def isvalid(s):
    parts = s.split(" ")
    t = parts[0]
    low = int(t[0 : t.find("-")])
    high = int(t[t.find("-") + 1 :])
    char = parts[1][0]
    p1 = parts[2][low - 1]
    p2 = parts[2][high - 1]
    if (char == p1 and char != p2) or (char != p1 and char == p2):
        return True
    else:
        return False


result = 0
for item in L:
    if isvalid(item):
        result += 1

print(f"Answer is: {result}")