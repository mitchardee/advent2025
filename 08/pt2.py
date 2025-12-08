from heapq import *
from math import dist, prod


nodes = [[int(y) for y in x.strip().split(',')] for x in open("testInput.txt").readlines()]

ret = 0

dists = [(dist(nodes[i], nodes[j]), i, j) for i in range(len(nodes) - 1) for j in range(i+1, len(nodes))]
heapify(dists)


circuit = [-1] * len(nodes)
circuits = []

while dists:
    _, a, b = heappop(dists)
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
        #Merge into lowest index circuit so we can always check circuits[0]
        if cB > cA:
            cB, cA = cA, cB
        for x in circuits[cA]:
            circuit[x] = cB
        circuits[cB] |= circuits[cA]
        circuits[cA] = None

    if len(circuits[0]) == len(nodes):
        print(nodes[a][0], nodes[b][0], nodes[a][0] * nodes[b][0])
        break