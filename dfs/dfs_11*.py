"""
백준 - 내리막 길
"""

import sys

sys.setrecursionlimit(10**6)


def dfs(x, y):
    if x == m - 1 and y == n - 1:
        return 1

    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if map[x][y] > map[nx][ny]:
            dp[x][y] += dfs(nx, ny)

    return dp[x][y]


def solution(x, y):
    return dfs(x, y)


if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    m, n = map(int, input().split())
    map = [list(map(int, input().split())) for _ in range(m)]
    dp = [[-1] * n for _ in range(m)]

    print(solution(0, 0))
