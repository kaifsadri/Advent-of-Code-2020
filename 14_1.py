P = [i.strip() for i in open("input_14.txt").readlines()]
# P = ["mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X", "mem[8] = 11", "mem[7] = 101", "mem[8] = 0"]

M = dict()
mask = ""
address = 0
value = 0


def bitmask(m, v):
    s = bin(v)[2:]
    s = "0" * (36 - len(s)) + s

    r = list()
    r = [s[i] if m[i] == "X" else m[i] for i in range(36)]
    r = "".join(r)
    return int(r, 2)


for line in P:
    if line.startswith("mask = "):
        mask = line[7:]
    if line.startswith("mem["):
        address = int(line.split(" = ")[0].split("[")[1][:-1])
        value = int(line.split(" = ")[1])
        M[address] = bitmask(mask, value)

print(sum(M.values()))