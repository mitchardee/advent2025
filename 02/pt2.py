lines = [x.strip() for x in open("input.txt").readlines()]
pairs = [[int(x) for x in pair.split('-')] for pair in lines[0].split(',')]

invalids = set()
m = str(max(p[1] for p in pairs))
ret = 0

for i in range(2, len(m)+1):
    for j in range(1, 10 ** (len(m)//i)):
        x = int(str(j) * i)
        if x not in invalids and any(a <= x <= b for [a, b] in pairs):
            ret += x
            invalids.add(x)

print(ret)