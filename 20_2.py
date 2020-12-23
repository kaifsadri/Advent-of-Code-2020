from collections import defaultdict

L = [line.strip() for line in open("input_20.txt").readlines()]


def top(tile):
    return tile[0]


def bottom(tile):
    return tile[-1]


def right(tile):
    return "".join([t[-1] for t in tile])


def left(tile):
    return "".join([t[0] for t in tile])


def rotate(tile):
    return list("".join(x[::-1]) for x in zip(*tile))


def flip(tile):
    return list("".join(x[::-1]) for x in tile)


def configs(tile):
    t1 = rotate(tile)
    t2 = rotate(t1)
    t3 = rotate(t2)
    return [tile, t1, t2, t3, flip(tile), flip(t1), flip(t2), flip(t3)]


Tiles = dict()
Edges = defaultdict(lambda: set())
for line in L:
    if "Tile" in line:
        tile = int(line[5:9])
        img = list()
        continue
    elif line:
        img.append(line)
    else:
        Tiles[tile] = img
        Edges[left(img)].add(tile)
        Edges[right(img)].add(tile)
        Edges[top(img)].add(tile)
        Edges[bottom(img)].add(tile)
        Edges[left(img)[::-1]].add(tile)
        Edges[right(img)[::-1]].add(tile)
        Edges[top(img)[::-1]].add(tile)
        Edges[bottom(img)[::-1]].add(tile)


Picture = dict()  # includes all the pixels for the final image
grid = dict()  # includes the relationships
D = int(len(Tiles) ** 0.5)
N = 8  # tiles are 10x10 with image being 8x8


def write_tile(tile, ROW, COL):  # position is (x,y on grid from bottom left corner)
    global Picture, N
    # strip the tile's borders
    t = [_[1:-1] for _ in tile[1:-1]]
    for row, _ in enumerate(t):
        for col, __ in enumerate(t[row]):
            Picture[(ROW * N + row, COL * N + col)] = __


for tile in Tiles:
    for t in configs(Tiles[tile]):
        if len(Edges[top(t)]) == 1 and len(Edges[left(t)]) == 1:
            grid[(0, 0)] = tile
            write_tile(t, 0, 0)
            Tiles[tile] = t
            break
        if (0, 0) in grid:
            break

for row in range(D):
    for col in range(D):
        if row == 0 and col == 0:
            c = Tiles[grid[(0, 0)]]
        elif col == 0:
            c = Tiles[grid[(row - 1, col)]]
            t = list(Edges[bottom(c)] - {grid[(row - 1, col)]})[0]
            for m in configs(Tiles[t]):
                if bottom(c) == top(m):
                    grid[(row, col)] = t
                    write_tile(m, row, col)
                    Tiles[t] = m
        else:
            c = Tiles[grid[(row, col - 1)]]
            t = list(Edges[right(c)] - {grid[(row, col - 1)]})[0]
            for m in configs(Tiles[t]):
                if left(m) == right(c):
                    grid[(row, col)] = t
                    write_tile(m, row, col)
                    Tiles[t] = m


Monster = ["                  # ", "#    ##    ##    ###", " #  #  #  #  #  #   "]

def is_monster(M, pix):
    global Picture
    Monster_mask = list()
    for row, _ in enumerate(M):
        for col, __ in enumerate(M[row]):
            if M[row][col] == "#":
                Monster_mask.append((row, col))
    try:
        for pixel in Monster_mask:
            if Picture[(pix[0] + pixel[0], pix[1] + pixel[1])] != "#":
                return False
    except KeyError:
        return False
    return True


NumMonsters = 0
Numhashes = 0

for pixel in Picture:
    if Picture[pixel] == "#":
        Numhashes += 1
    for m in configs(Monster):
        if is_monster(m, pixel):
            NumMonsters += 1

print(Numhashes - NumMonsters * ''.join(Monster).count('#'))
