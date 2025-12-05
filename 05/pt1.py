lines = [x.strip() for x in open("input.txt").readlines()]
i = next(i for i, line in enumerate(lines) if not line)
ranges = [x.split('-') for x in lines[:i]]
ranges = [(int(a), int(b)) for a, b in ranges]
inds = [int(x) for x in lines[i+1:]]

print(sum(any(a <= x <= b for (a, b) in ranges) for x in inds))