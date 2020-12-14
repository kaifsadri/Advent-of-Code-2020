L = [i.strip() for i in open("input_13.txt").readlines()]

A = int(L[0])
T = {int(t) for t in L[1].split(",") if t not in "xX"}

print(A, T)

t = A
found = False
times = list()

while True:
    for time in T:
        if t % time == 0:
            times.append((t - A, time))
    if len(times) == len(T):
        break
    t += 1

times.sort(key=lambda x: x[0])
print(times[0][0] * times[0][1])
