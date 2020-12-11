# L = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
L = open("input_02.txt").readlines()


def isvalid(s):
    parts = s.split(" ")
    t = parts[0]
    low = int(t[0 : t.find("-")])
    high = int(t[t.find("-") + 1 :])
    char = parts[1][0]
    cnt = parts[2].count(char)
    if low <= cnt and high >= cnt:
        return True
    else:
        return False


result = 0
for item in L:
    if isvalid(item):
        result += 1

print(f"Answer is: {result}")