lines = [x.strip().split() for x in open("input.txt").readlines()]
n = len(lines[0])
m = len(lines)
ret = 0

for i in range(n):
    if lines[-1][i] == '*':
        r = 1
        for j in range(m-1):
            r *= int(lines[j][i])
        ret += r
    else:
        r = 0
        for j in range(m-1):
            r += int(lines[j][i])
        ret += r

print(ret)