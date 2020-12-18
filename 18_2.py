L = [eq.replace(" ", "").strip() for eq in open("input_18.txt").readlines()]


def matching(eq):
    # find the matching ")" for an "("
    n = 0
    for pos, t in enumerate(eq[1:]):
        if n == 0 and t == ")":
            return pos + 0 + 1
        elif t == "(":
            n += 1
        elif t == ")":
            n -= 1
        else:
            pass


def eva(eq):
    result = 0
    op = "+"
    position = 0
    while position < len(eq):
        N = eq[position]
        if "0" <= N <= "9":
            if op == "+":
                result += int(N)
                position += 1
            elif op == "*":
                result *= int(N)
                position += 1
        elif N == "+":
            op = N
            position += 1
        elif N == "*":
            result *= eva(eq[position + 1 :])
            return result
        elif N == "(":
            m = matching(eq[position:])
            if op == "+":
                result += eva(eq[position + 1 : position + m])
            elif op == "*":
                result *= eva(eq[position + 1 : position + m])
            position += m + 1
    return result


print(sum([eva(r) for r in L]))