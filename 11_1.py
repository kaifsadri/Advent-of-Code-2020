Plane = [list(line.strip()) for line in open("input_11.txt").readlines()]
# Plane = [
#     "L.LL.LL.LL",
#     "LLLLLLL.LL",
#     "L.L.L..L..",
#     "LLLL.LL.LL",
#     "L.LL.LL.LL",
#     "L.LLLLL.LL",
#     "..L.L.....",
#     "LLLLLLLLLL",
#     "L.LLLLLL.L",
#     "L.LLLLL.LL",
# ]
W = len(Plane[0])
L = len(Plane)
Changed = True


def newSeat(plane, row, col):
    global Changed
    if plane[row][col] == ".":
        return ".", False
    seats = list()
    for r in [row - 1, row, row + 1]:
        for c in [col - 1, col, col + 1]:
            if r == row and c == col:
                pass
            elif not ((0 <= c < W) and (0 <= r < L)):
                pass
            elif "." == plane[r][c]:
                pass
            elif plane[r][c] == "#":
                seats.append(1)
            else:
                seats.append(0)
    if plane[row][col] == "#":
        if sum(seats) >= 4:
            return "L", True
        else:
            return "#", False
    elif plane[row][col] == "L":
        if sum(seats) == 0:
            return "#", True
        else:
            return "L", False
    else:
        print("ERROR!!!!!!!!!!!!!!")


while True:
    Changed = False
    NewP = []
    for row in range(L):
        NewP.append([])
        for col in range(W):
            result = newSeat(Plane, row, col)
            NewP[row].append(result[0])
            if result[1]:
                Changed = True
    Plane = NewP.copy()
    if not Changed:
        break

print(sum(row.count("#") for row in Plane))
