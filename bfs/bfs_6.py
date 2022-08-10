"""
백준 - 유기농 배추
"""

from collections import deque
from typing import List


def bfs(_x: int, _y: int):
    global cnt
    q = deque([(_x, _y)])
    visited[_x][_y] = True
    while q:
        coord = q.popleft()
        for _i in range(4):
            new_x, new_y = coord[0] + dx[_i], coord[1] + dy[_i]
            if new_x < 0 or new_x > n - 1 or new_y < 0 or new_y > m - 1:
                continue
            if mapping[new_x][new_y] == 1 and visited[new_x][new_y] is False:
                visited[new_x][new_y] = True
                q.append((new_x, new_y))


dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
rst = []
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    mapping: List[List[int]] = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        mapping[y][x] = 1

    visited: List[List[bool]] = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if mapping[i][j] == 1:
                if visited[i][j] is True:
                    continue
                bfs(i, j)
                cnt += 1
    rst.append(cnt)

for v in rst:
    print(v)
