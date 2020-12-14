L = [i.strip() for i in open("input_13.txt").readlines()]
Busses = [[i[0], int(i[1])] for i in enumerate(L[1].split(",")) if i[1] not in "xX"]
Busses.sort(key=lambda x: x[1], reverse=True)
# print(Busses)

# Bus frequencies are all prime numbers, so there is no overlap
# this is an implementation of a simplified sieving Chinese Remainder Theorem

TimeNow = 0
cycle = 1
for Offset, Frequency in Busses:
    while True:
        if (TimeNow + Offset) % Frequency == 0:
            break
        else:
            TimeNow += cycle
    cycle = cycle * Frequency

print(TimeNow)
