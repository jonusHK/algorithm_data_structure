import heapq

n = int(input())

heap = []
for _ in range(n):
    heapq.heappush(heap, int(input()))

s = 0
while len(heap) > 1:
    min_1 = heapq.heappop(heap)
    min_2 = heapq.heappop(heap)
    s_min = min_1 + min_2
    s += s_min
    heapq.heappush(heap, s_min)

print(s)
