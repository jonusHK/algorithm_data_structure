import heapq
from collections import defaultdict
from typing import List, Tuple, Dict, Set

edges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]


def prim(start_node: str):
    # 초기화
    mst = []
    adjacent_edges: Dict[str, Set[Tuple[int, str, str]]] = defaultdict(set)
    for edge in edges:
        adjacent_edges[edge[1]].add((edge[0], edge[1], edge[2]))
        adjacent_edges[edge[2]].add((edge[0], edge[2], edge[1]))

    candidated_edges: List[Tuple[int, str, str]] = list(adjacent_edges[start_node])
    connected_nodes: List[str] = [start_node]

    heapq.heapify(candidated_edges)
    while candidated_edges:
        edge = heapq.heappop(candidated_edges)
        if edge[2] not in connected_nodes:
            mst.append(edge)
            connected_nodes.append(edge[2])
            for _edge in adjacent_edges[edge[2]]:
                if _edge[2] not in connected_nodes:
                    heapq.heappush(candidated_edges, _edge)

    return mst


print(prim('A'))
