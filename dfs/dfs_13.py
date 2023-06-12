"""
백준 - 빙산
"""


import sys
from copy import deepcopy

sys.setrecursionlimit(10**4)


def dfs(x, y):
    visited[x][y] = 1

    minus_cnt = 0
    connected = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue

        if arr[nx][ny] == 0:
            minus_cnt += 1
        else:
            connected.append((nx, ny))

    temp[x][y] = temp[x][y] - minus_cnt if temp[x][y] > minus_cnt else 0

    height = temp[x][y]
    for nx, ny in connected:
        if not visited[nx][ny]:
            height += dfs(nx, ny)

    return height


def solution():
    global arr, visited

    year = 0
    while True:
        visited = [[0] * m for _ in range(n)]
        piece = 0
        height = 0
        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if not visited[i][j] and arr[i][j]:
                    if piece == 1:
                        return year

                    height += dfs(i, j)
                    piece += 1

        if not height:
            return 0

        arr = deepcopy(temp)
        year += 1


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    temp = deepcopy(arr)
    visited = [[0] * m for _ in range(n)]

    print(solution())
