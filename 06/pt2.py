from operator import add, mul

lines = [x for x in open("input.txt").readlines()]
breaks = [i for i in range(len(lines[-1])) if lines[-1][i].strip()] + [len(lines[0])]

ret = 0

for k in range(len(breaks) - 1):
    a, b = breaks[k:k+2]
    op = mul if lines[-1][a] == '*' else add
    r = 1 if lines[-1][a] == '*' else 0

    for i in range(a, b-1):
        x = 0
        for j in range(len(lines) - 1):
            if lines[j][i].isdigit():
                x *= 10
                x += int(lines[j][i])
        r = op(r, x)
    ret += r


print(ret)