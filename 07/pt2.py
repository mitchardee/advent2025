from typing import Counter


lines = [x.strip() for x in open("input.txt").readlines()]

ret = 0
beams = {lines[0].index('S') : 1}

for line in lines:
    nextBeams = Counter()
    for i, x in beams.items():
        if line[i] == '^':
            nextBeams[i-1] += x
            nextBeams[i+1] += x
        else:
            nextBeams[i] += x

    beams = nextBeams

print(sum(beams.values()))