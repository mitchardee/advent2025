lines = [[int(c) for c in x.strip()] for x in open("input.txt").readlines()]

ret = 0

for line in lines:
    prefs = [0] * 12
    for x in line:
        for i in range(11):
            prefs[i] = max(prefs[i], 10 * prefs[i+1] + x)
        prefs[11] = max(prefs[11], x)

    ret += prefs[0]

print(ret)