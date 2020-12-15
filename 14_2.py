P = [i.strip() for i in open("input_14.txt").readlines()]


def newaddr(adr, bits):
    m = adr
    for c in bits:
        m = m.replace("X", c, 1)
    return m


Mem = dict()
Addrs = list()
Mask = None

for line in P:
    if line.startswith("mask = "):
        Mask = line[7:]
    if line.startswith("mem["):
        address = bin(int(line.split(" = ")[0].split("[")[1][:-1]))[2:]
        address = "0" * (36 - len(address)) + address
        value = int(line.split(" = ")[1])

        r = list(address)
        for i in range(36):
            if Mask[i] == "X":
                r[i] = "X"
            if Mask[i] == "1":
                r[i] = "1"
        r = "".join(r)

        Addrs = list()
        for i in range(2 ** r.count("X")):
            t = bin(i)[2:]
            t = "0" * (r.count("X") - len(t)) + t
            Addrs.append(newaddr(r, t))

        for adr in Addrs:
            Mem[int(adr, 2)] = value

print(sum(Mem.values()))
