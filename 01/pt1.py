lines = [x.strip() for x in open("testInput.txt").readlines()]
pos = 50
ret = 0

for x in lines:
    a = int(x[1:])
    pos += (1 if x[0] == 'R' else -1) * a
    pos %= 100

    if not pos:
        ret += 1


print(ret)
