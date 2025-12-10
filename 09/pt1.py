points = [[int(y) for y in x.strip().split(',')] for x in open("input.txt").readlines()]
# for x in points:
#     print(x)

print(max(((abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)) for i in range(len(points)) for j in range(i+1, len(points))))
