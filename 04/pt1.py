lines = [x.strip() for x in open("input.txt").readlines()]

ret = 0

for i, line in enumerate(lines):
    for j, x in enumerate(line):
        if x == '@' and 5 > sum(lines[x][y] == '@' for x in range(max(0, i-1), min(len(lines), i+2)) for y in range(max(0, j-1), min(len(line), j+2))):
            ret += 1

print(ret)