lines = [list(x.strip()) for x in open("input.txt").readlines()]

ret = 0

def removable(i, j):
    return lines[i][j] == '@' and 5 > sum(inBounds(x, y) and lines[x][y] == '@' for x in range(i-1, i+2) for y in range(j-1, j+2))

def inBounds(i, j):
    return 0 <= i < len(lines) and 0 <= j < len(lines[i])

checkQ = []

for i in range(len(lines)):
    for j in range(len(lines[0])):
        if removable(i, j):
            ret += 1
            lines[i][j] = '.'
            checkQ.append((i, j))

while checkQ:
    nextQ = set()

    for (i, j) in checkQ:
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if inBounds(x, y) and removable(x, y):
                    ret += 1
                    lines[x][y] = '.'
                    nextQ.add((x, y))
    checkQ = nextQ


print(ret)