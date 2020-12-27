value = answer = 1
while value != 9659666:  # Puzzle input was 12320657, 9659666
    value = (7 * value) % 20201227
    answer = (12320657 * answer) % 20201227
print(answer)
