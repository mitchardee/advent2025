from functools import cache


lines = [x.strip().split() for x in open("input.txt").readlines()]

outs = {}
for line in lines:
    outs[line[0][:-1]] = line[1:]

@cache
def dfs(s, fft, dac):
    if s == 'out':
        return int(fft and dac)
    return sum(dfs(v, fft or s == 'fft', dac or s == 'dac') for v in outs[s])

print(dfs('svr', False, False))