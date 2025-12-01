lines = [x.strip() for x in open("input.txt").readlines()]
pos = 50
ret = 0

for x in lines:
    pos = (pos + (2 * (x[0] == 'R') - 1) * int(x[1:])) % 100
    ret += not pos

print(ret)