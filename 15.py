from collections import deque, defaultdict

L = [7, 14, 0, 17, 11, 1, 2]
# L = [0, 3, 6]

History = defaultdict(lambda: deque([0, 0], 2))
Turn = 1
Last = None
Starting = True

while True:
    if L:
        j = L.pop(0)
        History[j].append(Turn)
        Last = j
    elif Last in History and 0 not in History[Last]:
        Last = History[Last][1] - History[Last][0]
        History[Last].append(Turn)
    else:
        Last = 0
        History[0].append(Turn)
    Turn += 1
    # Output
    if Turn == 2020 + 1:
        print(f"Part 1: {Last}")
    elif Turn == 30000000 + 1:
        print(f"Part 2: {Last}")
        break
