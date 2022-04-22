"""
백준 - 문제집 (위상정렬)
"""

import heapq
import sys

n, m = map(int, sys.stdin.readline().split())

array = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]

for i in range(m):
    x, y = map(int, sys.stdin.readline().split())
    array[x].append(y)
    indegree[y] += 1

heap = []
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(heap, i)

result = []
while heap:
    data = heapq.heappop(heap)
    result.append(data)
    if array[data]:
        for y in array[data]:
            indegree[y] -= 1
            if indegree[y] == 0:
                heapq.heappush(heap, y)

for num in result:
    print(num, end=' ')
