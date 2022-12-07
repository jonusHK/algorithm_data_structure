"""
최소 신장 트리 (프림 알고리즘)
"""

# 중복된 노드에 연결된 간선은 제거
import heapq
from collections import defaultdict

graph = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]


def prim(start_node: str):
    mst = []

    # 초기화
    connected_nodes = set(start_node)
    adjacent_edges = defaultdict(list)
    for w, node_u, node_v in graph:
        adjacent_edges[node_u].append((w, node_u, node_v))
        adjacent_edges[node_v].append((w, node_v, node_u))

    candidated_edges = adjacent_edges[start_node]
    heapq.heapify(candidated_edges)
    # 추천 경로에서 가중치가 제일 낮은 경로를 가져와서 연결되지 않았으면 경로 추가
    while candidated_edges:
        edge = heapq.heappop(candidated_edges)
        if edge[2] not in connected_nodes:
            mst.append(edge)
            connected_nodes.add(edge[2])
            for _edge in adjacent_edges[edge[2]]:
                if _edge[2] not in connected_nodes:
                    heapq.heappush(candidated_edges, _edge)

    return mst


print(prim('A'))
