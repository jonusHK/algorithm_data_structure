"""
백준 - 거의 최단 경로
"""
import heapq
import sys
from typing import List, Tuple

_input = sys.stdin.readline


def dijkstra(mapping: List[List[Tuple[int, int]]], dist: List[int], start: int, flag=0):
    dist[start] = 0
    q = [(dist[start], start)]

    while q:
        cur_dist, cur_num = heapq.heappop(q)
        if dist[cur_num] < cur_dist:
            continue

        for next_dist, next_num in mapping[cur_num]:
            if flag and dist_1[cur_num] + next_dist + dist_2[next_num] == dist_1[d]:
                continue

            new_dist = cur_dist + next_dist
            if new_dist < dist[next_num]:
                dist[next_num] = new_dist
                heapq.heappush(q, (new_dist, next_num))


while True:
    n, m = map(int, _input().split())
    if n == 0:
        break
    s, d = map(int, _input().split())

    adj: List[List[Tuple[int, int]]] = [[] for _ in range(n)]
    reverse_adj: List[List[Tuple[int, int]]] = [[] for _ in range(n)]

    for _ in range(m):
        u, v, p = map(int, _input().split())
        adj[u].append((p, v))
        reverse_adj[v].append((p, u))

    dist_1, dist_2, dist_3 = [1e9] * n, [1e9] * n, [1e9] * n

    dijkstra(adj, dist_1, s)
    dijkstra(reverse_adj, dist_2, d)
    dijkstra(adj, dist_3, s, 1)

    print(dist_3[d] if dist_3[d] != 1e9 else -1)
