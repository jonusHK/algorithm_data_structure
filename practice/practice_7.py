graph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}
parent, rank = {}, {}


def find(node: str):
    while parent[node] != node:
        node = parent[node]
    return parent[node]


def union(node_a: str, node_b: str):
    root_a, root_b = find(node_a), find(node_b)
    if rank[root_a] > rank[root_b]:
        parent[root_b] = root_a
    elif rank[root_a] < rank[root_b]:
        parent[root_a] = root_b
    else:
        rank[root_a] += 1
        parent[root_b] = root_a


def kruskal():
    # 초기화
    mst = []
    graph['edges'].sort()
    for n in graph['vertices']:
        parent[n] = n
        rank[n] = 1

    for w, a, b in graph['edges']:
        if find(a) != find(b):
            union(a, b)
            mst.append((w, a, b))

    return mst


print(kruskal())
