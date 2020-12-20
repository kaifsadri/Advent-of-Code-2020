from collections import defaultdict

L = [line.strip() for line in open("input_20.txt").readlines()]

Tiles = dict()

for line in L:
    if "Tile" in line:
        tile = int(line[5:9])
        Tiles[tile] = set()
        img = list()
        continue
    elif line:
        img.append(line)
    else:
        edges = list()
        edges.append(img[0])
        edges.append("".join([_[-1] for _ in img]))
        edges.append(img[-1])
        edges.append("".join([_[0] for _ in img]))
        for e in edges:
            Tiles[tile].add(e)
            Tiles[tile].add(e[::-1])

Edges = defaultdict(set)
for t in Tiles:
    for e in Tiles[t]:
        Edges[e].add(t)

Corners = list()
for t in Tiles:
    n = 0
    for e in Tiles[t]:
        if len(Edges[e]) == 1:
            n += 1
    if n == 4:
        Corners.append(t)

print(Corners[0] * Corners[1] * Corners[2] * Corners[3])
