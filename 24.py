from collections import Counter

PUZZLE = [line.strip() for line in open("input_24.txt").readlines()]
black = set()
D = {
    "ne": (1, -1),
    "e": (1, 0),
    "se": (0, 1),
    "sw": (-1, 1),
    "w": (-1, 0),
    "nw": (0, -1),
}
for line in PUZZLE:
    tile = list(line)
    coord = (0, 0)
    while tile:
        m = tile.pop(0)
        if m in "ns":
            m += tile.pop(0)
        d = D[m]
        coord = (coord[0] + d[0], coord[1] + d[1])
    if coord in black:
        black.remove(coord)
    else:
        black.add(coord)
print(f"Part 1: {len(black)}")

for day in range(1, 101):
    wt_nbs = Counter()
    flip_black = set()
    for tile in black:
        N = 0
        for nb in [(tile[0] + d[0], tile[1] + d[1]) for d in D.values()]:
            if nb in black:
                N += 1
            else:
                wt_nbs[nb] += 1
        if N > 2 or N == 0:
            flip_black.add(tile)
    for tile in flip_black:
        black.remove(tile)
    for tile in wt_nbs:
        if wt_nbs[tile] == 2:
            black.add(tile)
print(f"Part 2: {len(black)}")