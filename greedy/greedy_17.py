"""
백준 - 행렬
"""

from typing import List

n, m = map(int, input().split())

array_a = [list(map(int, list(input()))) for _ in range(n)]
array_b = [list(map(int, list(input()))) for _ in range(n)]


def flip(_array: List[List[int]], x: int, y: int, length=3):
    for _i in range(length):
        for _j in range(length):
            _array[x + _i][y + _j] = 0 if _array[x + _i][y + _j] == 1 else 1


cnt = 0
for i in range(n - 2):
    for j in range(m - 2):
        if array_a[i][j] != array_b[i][j]:
            flip(array_a, i, j)
            cnt += 1

if array_a != array_b:
    print(-1)
else:
    print(cnt)
