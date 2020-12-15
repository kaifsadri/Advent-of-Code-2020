P = [line.strip() for line in open("input_08.txt").readlines()]

prev = set()
num = 0
accum = 0
while True:
    if num in prev:
        break
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
print(accum)
