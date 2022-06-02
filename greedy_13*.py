"""
백준 - 컵라면
"""

import heapq
import sys


input_ = sys.stdin.readline

n = int(input_())
array = []
for _ in range(n):
    d, cnt = map(int, input_().split())
    array.append((d, cnt))

array.sort()

q = []
for d, cnt in array:
    heapq.heappush(q, cnt)
    if len(q) > d:
        heapq.heappop(q)

print(sum(q))
