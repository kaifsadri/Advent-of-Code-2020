from math import prod


L = [line.strip() for line in open("input_16.txt").readlines()]

Criteria = dict()
i = 0
line = L[i]
while line:
    criterion, ranges = line.split(": ")
    Criteria[criterion] = set()
    r = ranges.split(" or ")
    for nums in r:
        num = nums.split("-")
        num0 = int(num[0])
        num1 = int(num[1])
        Criteria[criterion] = Criteria[criterion].union(set(range(num0, num1 + 1)))
    i += 1
    line = L[i]

i = sum([n + 1 for n, line in enumerate(L) if line.startswith("your")])
YourTicket = list(map(int, L[i].split(",")))

i = sum([n + 1 for n, line in enumerate(L) if line.startswith("nearby")])
T = [list(map(int, ticket.split(","))) for ticket in L[i:]]
GoodCrits = []
GoodTics = list()

for t in [YourTicket] + T:
    line = list()
    for j in t:
        s = {crit for crit in Criteria if j in Criteria[crit]}
        line.append(s)
    if set() not in line:
        GoodCrits.append(line)
        GoodTics.append(t)

arrangement = list()
for index in range(len(YourTicket)):
    c = set.intersection(*[gc[index] for gc in GoodCrits])
    arrangement.append([index, len(c), list(c)])

arrangement.sort(key=lambda x: x[1])

Final = list()
for index, item in enumerate(arrangement):
    Final.append([item[0], item[2]])
    for j in arrangement[index + 1 :]:
        j[2].remove(item[2][0])

TICKET = dict(zip([i[1][0] for i in sorted(Final, key=lambda x: x[0])], YourTicket))

print(prod([TICKET[i] for i in TICKET if i.startswith("departure")]))