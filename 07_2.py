T = [
    "light red bags contain 1 bright white bag, 2 muted yellow bags.\n",
    "dark orange bags contain 3 bright white bags, 4 muted yellow bags.\n",
    "bright white bags contain 1 shiny gold bag.\n",
    "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.\n",
    "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.\n",
    "dark olive bags contain 3 faded blue bags, 4 dotted black bags.\n",
    "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.\n",
    "faded blue bags contain no other bags.\n",
    "dotted black bags contain no other bags.\n",
]

L = [
    line.strip()
    .replace(" no other bags", "")
    .replace(" bags", "")
    .replace(" bag", "")
    .replace(",", "")
    .replace(".", "")
    .replace(" contain", "")
    .split(" ")
    for line in open("input_07.txt").readlines()
    # for line in T
]

S = dict()
for line in L:
    B = line[0] + " " + line[1]
    if len(line) > 2:
        for i in range(len(line[2:]) // 3):
            bag = line[2 + i * 3 + 1] + " " + line[2 + i * 3 + 2]
            num = int(line[2 + i * 3])
            try:
                S[B][bag] = num
            except KeyError:
                S[B] = {bag: num}


def numbags(s):
    try:
        bags = S[s]
    except KeyError:
        return 0
    return sum([numbags(bag) * bags[bag] for bag in bags.keys()]) + sum(bags.values())


print(numbags("shiny gold"))