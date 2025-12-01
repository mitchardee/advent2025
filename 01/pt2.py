lines = [x.strip() for x in open("input.txt").readlines()]
pos = 50
ret = 0

for x in lines:
    a = int(x[1:])
    ret += a // 100
    a %= 100

    newPos = pos + (1 if x[0] == 'R' else -1) * a

    if (newPos <= 0 and pos > 0) or newPos >= 100:
        ret += 1

    pos = newPos % 100

print(ret)
