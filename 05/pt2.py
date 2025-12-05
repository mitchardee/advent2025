lines = [x.strip() for x in open("input.txt").readlines()]
i = next(i for i, line in enumerate(lines) if not line)
ranges = [x.split('-') for x in lines[:i]]
ranges = [(int(a), int(b)) for a, b in ranges]
ranges.sort()

l, r = ranges[0]
ret = 0

for a, b in ranges:
    if r >= a-1:
        r = max(r, b)
    else:
        ret += r - l + 1
        l, r = a, b

ret += r - l + 1
print(ret)