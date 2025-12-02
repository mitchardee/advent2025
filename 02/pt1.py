lines = [x.strip() for x in open("testInput.txt").readlines()]
pairs = [[int(x) for x in pair.split('-')] for pair in lines[0].split(',')]

m = str(max(p[1] for p in pairs))
ret = 0
for i in range(1, int(m[:len(m)//2])+1):
    x = int(str(i) * 2)
    if any(a <= x <= b for [a, b] in pairs):
        ret += x

print(ret)