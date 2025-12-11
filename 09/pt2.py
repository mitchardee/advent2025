points = [[int(y) for y in x.strip().split(',')] for x in open("input.txt").readlines()]

xCoords = sorted({y for x, _ in points for y in range(x-1, x+2)})
yCoords = sorted({y for _, x in points for y in range(x-1, x+2)})

#Compress the inputs by only using values that're in the input, +/- 1 on either side
ordToValX = {i : x for i, x in enumerate(xCoords)}
valToOrdX = {x : i for i, x in enumerate(xCoords)}

ordToValY = {i : x for i, x in enumerate(yCoords)}
valToOrdY = {x : i for i, x in enumerate(yCoords)}


#Points converted to their ordinal values to compress the board
ordPoints = [(valToOrdX[x], valToOrdY[y]) for x, y in points]

grid = [[1] * len(yCoords) for _ in xCoords]


#Create the lines between points on the ordinal graph
for i in range(len(ordPoints)):
    j = (i + 1) % len(ordPoints)
    xi, yi = ordPoints[i]
    xj, yj = ordPoints[j]

    if xi == xj:
        if yi > yj:
            yi, yj = yj, yi
        
        for k in range(yi, yj+1):
            grid[xi][k] = 2
    else:
        if xi > xj:
            xi, xj = xj, xi
        
        for k in range(xi, xj+1):
            grid[k][yi] = 2

#Flood fill the ordinal graph to remove everything not inside the lines
q = [(0,0)]
dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
while q:
    nextQ = set()
    for x, y in q:
        if grid[x][y] == 1:
            grid[x][y] = 0
            for dx, dy in dirs:
                if 0 <= x+dx < len(xCoords) and 0 <= y+dy < len(yCoords):
                    nextQ.add((x + dx, y + dy))
    q = nextQ

ret = 0

#Convert the ordinal coordinates to area
def ordToArea(xi, yi, xj, yj):
    return (abs(ordToValX[xi] - ordToValX[xj]) + 1) * (abs(ordToValY[yi] - ordToValY[yj]) + 1)

for i in range(len(ordPoints) - 1):
    for j in range(i, len(ordPoints)):
        xi, yi = ordPoints[i]
        xj, yj = ordPoints[j]

        a = ordToArea(xi, yi, xj, yj)
        if a > ret:
            #Check everywhere in the flood-filled graph to make sure each index is within the bounds
            if all(grid[x][y] for x in range(min(xi, xj), max(xi, xj) + 1) for y in range(min(yi, yj), max(yi, yj) + 1)):
                ret = a

print(ret)