"""
백준 - 문제집
"""
import heapq
import sys
from typing import List

_input = sys.stdin.readline

n, m = map(int, _input().split())

mapping: List[List[int]] = []
indegree: List[int] = []
for _ in range(n + 1):
    mapping.append([])
    indegree.append(0)

for _ in range(m):
    a, b = map(int, _input().split())
    mapping[a].append(b)
    indegree[b] += 1

heap = []
for i, v in enumerate(indegree):
    if i != 0 and v == 0:
        heapq.heappush(heap, i)

results = []
while heap:
    num = heapq.heappop(heap)
    results.append(num)
    for next_num in mapping[num]:
        indegree[next_num] -= 1
        if indegree[next_num] == 0:
            heapq.heappush(heap, next_num)

for r in results:
    print(r, end=' ')
