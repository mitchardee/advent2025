lines = [[int(c) for c in x.strip()] for x in open("input.txt").readlines()]

ret = 0

for line in lines:
    a = 0
    r = 0
    for x in line:
        r = max(r, a * 10 + x)
        a = max(a, x)
    ret += r

print(ret)