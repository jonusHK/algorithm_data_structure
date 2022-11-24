"""
백준 - 소수의 곱
"""

import heapq
from copy import deepcopy

k, n = map(int, input().split())
array = list(map(int, input().split()))

copied, checked = deepcopy(array), set()

heapq.heapify(copied)
ith = 0

while ith < n:
    v = heapq.heappop(copied)
    if v in checked:
        continue
    ith += 1
    checked.add(v)
    for i in array:
        if v * i < 2 ** 32:
            heapq.heappush(copied, v * i)

print(v)
