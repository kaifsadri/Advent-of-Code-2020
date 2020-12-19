import re

L = [line.strip() for line in open("input_19.txt").readlines()]
R = dict()
for marker, line in enumerate(L):
    if not line:
        break
    k, v = line.split(": ")
    R[k] = v.split(" ")


def cpl(r):
    global R
    result = "("
    for item in R[r]:
        if item == '"a"':
            result += "a"
        elif item == '"b"':
            result += "b"
        elif item == "|":
            result += ")|("
            pass
        else:
            result += "(" + cpl(item) + ")"
    result += ")"
    return result


p = re.compile(cpl("0"))
print(sum([1 for i in L[marker + 1 :] if re.fullmatch(p, i)]))
