Prog = [line.strip() for line in open("input_08.txt").readlines()]


def run(P):
    prev = set()
    num = 0
    accum = 0
    while True:
        if num >= len(P) - 1:
            return accum
        if num in prev:
            return False
        instr, value = P[num].split(" ")
        value = int(value)
        if instr == "acc":
            accum += value
            prev.add(num)
            num += 1
        elif instr == "nop":
            prev.add(num)
            num += 1
        elif instr == "jmp":
            prev.add(num)
            num += value


Test = [list(line) for line in enumerate(Prog) if line[1][0:2] in "nopjmp" and line[1][-1] != "0"]

for T in Test:
    O = Prog.copy()
    if T[1].startswith("jmp"):
        T[1] = "nop" + T[1][3:]
    elif T[1].startswith("nop"):
        T[1] = "jmp" + T[1][3:]
    O[T[0]] = T[1]
    A = run(O)
    if A:
        print(A)
        break
