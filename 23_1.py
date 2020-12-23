CUPS = [int(_) for _ in list("496138527")]


def move():
    global CUPS
    c = CUPS.copy()
    picked = list()

    for _ in range(3):
        picked.append(c.pop(1))

    dest_no = c[0] - 1 if c[0] > 1 else max(c)
    dest_idx = 0
    while True:True
        try:
            dest_idx = c.index(dest_no)
            break
        except ValueError:
            dest_no -= 1
            if dest_no < 1:
                dest_no = max(c)

    for _ in picked[::-1]:
        c.insert(dest_idx + 1, _)

    c.append(c.pop(0))
    CUPS = c


if __name__ == "__main__":
    for i in range(100):
        move()
    ans = CUPS[CUPS.index(1) + 1 :] + CUPS[0 : CUPS.index(1)]
    print("".join([str(_) for _ in ans]))
