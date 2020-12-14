P = [i.strip() for i in open("input_12.txt").readlines()]
Location = [0, 0]  # x,y
Direction = [1, 0]  # unit vector pointing to direction

Turns = {"L": [-1, 1], "R": [1, -1]}
Moves = {"E": [1, 0], "N": [0, 1], "W": [-1, 0], "S": [0, -1]}


def turn(d, t, a):
    if 180 == a:
        return [-d[0], -d[1]]
    elif 90 == a:
        return [d[1] * Turns[t][0], d[0] * Turns[t][1]]
    elif 270 == a:
        # 270 = 90 in other direction:
        e = "R" if "L" == t else "L"
        return turn(d, e, 90)
    else:
        print("WRONG TURN!")


def move(l, v, m):
    return [l[0] + v * Moves[m][0], l[1] + v * Moves[m][1]]


for line in P:
    Instruction = line[0]
    Value = int(line[1:])
    if Instruction in "NESW":
        Location = move(Location, Value, Instruction)
    elif Instruction in "LR":
        Direction = turn(
            Direction,
            Instruction,
            Value,
        )
    elif Instruction == "F":
        Location = [Location[0] + Value * Direction[0], Location[1] + Value * Direction[1]]
    else:
        print(f"Wrong Instruction: {line}")

print(abs(Location[0]) + abs(Location[1]))
