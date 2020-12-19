import re
from collections import Counter

L = [line.strip() for line in open("input_19.txt").readlines()]
R = dict()
for marker, line in enumerate(L):
    if not line:
        break
    k, v = line.split(": ")
    R[k] = v.split(" ")
R["8"] = ["42", "|", "42", "8"]
R["11"] = ["42", "31", "|", "42", "11", "31"]


# This is a hack to limit the number of recursions on 8 and 11.
# Only need to rerun for a few iterations.

MAXR = 20
RECUR = Counter()


def cpl(r):
    global R, RECUR
    result = "("
    for item in R[r]:
        if item == '"a"':
            result += "a"
        elif item == '"b"':
            result += "b"
        elif item == "|":
            result += ")|("
            pass
        elif item != r:
            result += "(" + cpl(item) + ")"
        else:
            if RECUR[r] < MAXR:
                RECUR[r] += 1
                result += "(" + cpl(item) + ")"
            else:
                pass
    result += ")"
    return result


p = re.compile(cpl("0"))
print(sum([1 for i in L[marker + 1 :] if re.fullmatch(p, i)]))
