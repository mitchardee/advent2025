lines = [x.strip() for x in open("input.txt").readlines()]

ret = 0
beams = [lines[0].index('S')]

for line in lines:
    nextBeams = set()
    for i in beams:
        if line[i] == '^':
            nextBeams.add(i-1)
            nextBeams.add(i+1)
            ret += 1
        else:
            nextBeams.add(i)

    beams = nextBeams

print(ret)