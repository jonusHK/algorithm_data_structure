"""
프로그래머스 - 네트워크
"""

from typing import Dict, List


def find(mapper: Dict[int, int], node: int):
    while mapper[node] != node:
        node = mapper[node]
    return node


def union(mapper: Dict[int, int], rank: List[int], root_u: int, root_v: int) -> int:
    if rank[root_u] > rank[root_v]:
        mapper[root_v] = root_u
    else:
        mapper[root_u] = root_v
        if rank[root_u] == rank[root_v]:
            rank[root_v] += 1


def solution(n, computers):
    rank = [1 for _ in range(n)]
    mapper = {
        i: i for i in range(n)
    }

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i == j:
                continue
            if computers[i][j] == 1:
                union(mapper, rank, find(mapper, i), find(mapper, j))
                computers[j][i] = 0

    result = set()
    for k in mapper.keys():
        result.add(find(mapper, k))

    return len(result)


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
