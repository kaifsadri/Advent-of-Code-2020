P = [i.strip() for i in open("input_12.txt").readlines()]
Location = [0, 0]  # x,y
WayPoint = [10, 1]

Turns = {"L": [-1, 1], "R": [1, -1]}
Moves = {"E": [1, 0], "N": [0, 1], "W": [-1, 0], "S": [0, -1]}


def turn(wp, t, a):
    if 180 == a:
        return [-wp[0], -wp[1]]
    elif 90 == a:
        return [wp[1] * Turns[t][0], wp[0] * Turns[t][1]]
    elif 270 == a:
        # 270 = 90 in other direction:
        d = "R" if "L" == t else "L"
        return turn(wp, d, 90)
    else:
        print(f"WRONG TURN! {t} , {a}")


def move(wp, v, m):
    return [wp[0] + v * Moves[m][0], wp[1] + v * Moves[m][1]]


for line in P:
    Instruction = line[0]
    Value = int(line[1:])
    if Instruction in "NESW":
        WayPoint = move(WayPoint, Value, Instruction)
    elif Instruction in "LR":
        WayPoint = turn(
            WayPoint,
            Instruction,
            Value,
        )
    elif Instruction == "F":
        Location = [Location[0] + Value * WayPoint[0], Location[1] + Value * WayPoint[1]]
    else:
        print(f"Wrong Instruction: {line}")

print(abs(Location[0]) + abs(Location[1]))
