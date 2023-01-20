import heapq
import sys
from copy import deepcopy

_input = sys.stdin.readline

k, n = map(int, _input().split())
array = list(map(int, _input().split()))


q = deepcopy(array)
heapq.heapify(q)

checked = set()
nth, v = 0, 0

while nth < n:
    v = heapq.heappop(q)
    if v in checked:
        continue
    nth += 1
    checked.add(v)
    for i in array:
        num = i * v
        if num < 2 ** 32:
            heapq.heappush(q, num)

print(v)
