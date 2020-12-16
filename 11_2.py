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
    for i in [-1, 0, +1]:
        for j in [-1, 0, +1]:
            # (i,j) defines the direction. Now need to scan in this direction for the first seat to see
            for k in range(1, L + W):  # large enough to reach the end of the plane
                r = row + k * i
                c = col + k * j
                if not ((0 <= c < W) and (0 <= r < L)):
                    # hit the wall
                    break
                elif r == row and c == col:
                    break
                elif "." == plane[r][c]:
                    # look on
                    continue
                elif plane[r][c] == "L":
                    # No need to do anything - just break
                    break
                elif plane[r][c] == "#":
                    seats.append(1)
                    break
    if plane[row][col] == "#":
        if sum(seats) >= 5:
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
