from itertools import permutations
from math import sqrt


def calc_dist(tu_1: tuple, tu_2: tuple):
    diff_x = tu_1[0] - tu_2[0]
    diff_y = tu_1[1] - tu_2[1]

    return sqrt(diff_x ** 2 + diff_y ** 2)


def find(node: int):
    if parent[node] != node:
        parent[node] = find(parent[node])

    return parent[node]


def union(_node_u: int, _node_v: int):
    root_u = find(_node_u)
    root_v = find(_node_v)
    if rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_u] = root_v
        if rank[root_u] == rank[root_v]:
            rank[root_v] += 1


n, m = map(int, input().split())

nodes = [None]
edges = []
parent = [v for v in range(0, n + 1)]
rank = [1] * (n + 1)

for _ in range(n):
    x, y = map(int, input().split())
    nodes.append((x, y))

perms = list(permutations(parent[1:], 2))
for perm in perms:
    dist = calc_dist(nodes[perm[0]], nodes[perm[1]])
    edges.append((dist, perm[0], perm[1]))

for _ in range(m):
    n1, n2 = map(int, input().split())
    if find(n1) != find(n2):
        union(n1, n2)

edges.sort()

shortest_dist = 0
for edge in edges:
    dist, node_u, node_v = edge
    if find(node_u) != find(node_v):
        union(node_u, node_v)
        shortest_dist += dist

print("{:.2f}".format(shortest_dist))
