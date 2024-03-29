mygraph = {
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
parent, rank = dict(), dict()


def find(n):
    # path compression 기법
    if parent[n] != n:
        parent[n] = find(parent[n])

    return parent[n]


def union(n1, n2):
    root1 = find(n1)
    root2 = find(n2)

    # union-by-rank 기법
    if rank[root1] < rank[root2]:
        parent[root1] = root2
    else:
        parent[root2] = root1
        if rank[root1] == rank[root2]:
            rank[root1] += 1


def kruskal(graph):
    mst = list()

    # 1. 초기화
    for n in graph['vertices']:
        parent[n] = n
        rank[n] = 0

    # 2. 간선 weight 기반 sorting
    edges = graph['edges']
    edges.sort()

    # 3. 사이클 없는 간선만 연결
    for edge in edges:
        weight, n1, n2 = edge
        if find(n1) != find(n2):
            union(n1, n2)
            mst.append((weight, n1, n2))

    return mst


print(kruskal(mygraph))