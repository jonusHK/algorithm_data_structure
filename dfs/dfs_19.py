"""
백준 - 안전 영역
"""


import sys

sys.setrecursionlimit(10**6)


def dfs(x, y, h, visited):

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if visited[nx][ny]:
            continue

        if arr[nx][ny] <= h:
            continue

        dfs(nx, ny, h, visited)


def solution(n, max_v, min_v):

    max_cnt = 0
    for h in range(min_v, max_v):

        cnt = 0
        visited = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if visited[i][j]:
                    continue

                if arr[i][j] <= h:
                    continue

                dfs(i, j, h, visited)
                cnt += 1

        max_cnt = max(max_cnt, cnt)

    return max_cnt or 1


if __name__ == "__main__":
    n = int(input())

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    arr = []
    max_v = 0
    min_v = float('inf')

    for _ in range(n):
        row = list(map(int, input().split()))
        max_v = max(max_v, max(row))
        min_v = min(min_v, min(row))
        arr.append(row)

    print(solution(n, max_v, min_v))
