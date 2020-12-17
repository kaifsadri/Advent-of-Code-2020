L = [line.strip() for line in open("input_16.txt").readlines()]

Criteria = set()

i = 0
line = L[i]
while line:
    criterion, ranges = line.split(": ")
    r = ranges.split(" or ")
    for nums in r:
        num = nums.split("-")
        num0 = int(num[0])
        num1 = int(num[1])
        Criteria = Criteria.union(set(range(num0, num1 + 1)))
    i += 1
    line = L[i]

Error_rate = 0

# first ticket
i = sum([n + 1 for n, line in enumerate(L) if line.startswith("nearby")])
for ticket in L[i:]:
    nums = [int(value) for value in ticket.split(",")]
    for n in nums:
        if n not in Criteria:
            Error_rate += n

print(Error_rate)