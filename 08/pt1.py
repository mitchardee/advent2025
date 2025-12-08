from heapq import nlargest, nsmallest
from math import dist, prod


nodes = [[int(y) for y in x.strip().split(',')] for x in open("input.txt").readlines()]
connections = 1000

ret = 0

dists = [(dist(nodes[i], nodes[j]), i, j) for i in range(len(nodes) - 1) for j in range(i+1, len(nodes))]
conns = nsmallest(connections, dists)


circuit = [-1] * len(nodes)
circuits = []

for _, a, b in conns:
    cA, cB = circuit[a], circuit[b]
    if cA == cB:
        if cA == -1:
            circuit[a] = len(circuits)
            circuit[b] = len(circuits)
            circuits.append({a, b})
    elif cB == -1:
        circuit[b] = cA
        circuits[cA].add(b)
    elif cA == -1:
        circuit[a] = cB
        circuits[cB].add(a)
    else:
        for x in circuits[cA]:
            circuit[x] = cB
        circuits[cB] |= circuits[cA]
        circuits[cA] = None


# print(circuit)
# print(circuits)
ret = nlargest(3, [len(x) if x else 0 for x in circuits])

print(ret, prod(ret))