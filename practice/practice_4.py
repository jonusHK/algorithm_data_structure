"""
최소 신장 트리 (크루스칼 알고리즘)
"""

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


def make_set(node: str):
    parent[node] = node
    rank[node] = 1


def find(node: str):
    # 방법1) 반복문
    while parent[node] != node:
        node = parent[node]
    # 방법2) 재귀함수
    # if parent[node] != node:
    #     parent[node] = find(parent[node])
    return parent[node]


def union(node_u: str, node_v: str):
    root_node_u = find(node_u)
    root_node_v = find(node_v)
    if rank[root_node_u] > rank[root_node_v]:
        parent[root_node_v] = root_node_u
    elif rank[root_node_u] < rank[root_node_v]:
        parent[root_node_u] = root_node_v
    else:
        rank[root_node_u] += 1
        parent[root_node_v] = root_node_u


def kruskal():
    mst = []

    # 초기화
    for n in graph['vertices']:
        make_set(n)

    # 간선 가중치 기반 Sorting
    graph['edges'].sort()

    # 사이클 없는 간선만 연결
    for w, node_u, node_v in graph['edges']:
        if find(node_u) != find(node_v):
            union(node_u, node_v)
            mst.append((w, node_u, node_v))

    return mst


print(kruskal())

