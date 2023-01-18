"""
백준 - 컵라면
"""
import heapq

n = int(input())

array = []
for _ in range(n):
    d, c = map(int, input().split())
    array.append((d, c))

array.sort()

heap = []
for deadline, cnt in array:
    heapq.heappush(heap, cnt)
    if len(heap) > deadline:
        heapq.heappop(heap)

print(sum(heap))
