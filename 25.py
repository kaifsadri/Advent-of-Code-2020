K = [12320657, 9659666]  # Puzzle input
M = 20201227

# Transform function is equivalent to python's pow(7, loop, 20201227)
# but finding by increasing the loop one by one is faster O(n)
loop = 0
value = 1
while value != K[1]:  # Choosing the smaller key, but not sure it will be faster
    value = (7 * value) % M
    loop += 1

print(pow(K[0], loop, M))
