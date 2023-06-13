"""
백준 - 알고리즘 수업 - 깊이 우선 탐색 1
"""

import heapq
import sys

sys.setrecursionlimit(10**5)


def dfs(v, order):
    visited[v] = order

    while graph[v]:
        nv = heapq.heappop(graph[v])

        if not visited[nv]:
            order = dfs(nv, order + 1)

    return order


def solution(start):
    dfs(start, 1)

    for i in range(1, n + 1):
        print(visited[i])


if __name__ == "__main__":
    n, m, r = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    map(lambda x: heapq.heapify(x), graph)
    visited = [0] * (n + 1)

    for _ in range(m):
        u, v = map(int, input().split())
        heapq.heappush(graph[u], v)
        heapq.heappush(graph[v], u)

    solution(r)
