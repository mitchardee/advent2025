from functools import cache


lines = [x.strip().split() for x in open("input.txt").readlines()]

outs = {}
for line in lines:
    outs[line[0][:-1]] = line[1:]

@cache
def dfs(s):
    if s == 'out':
        return 1
    return sum(dfs(v) for v in outs[s])

print(dfs('you'))