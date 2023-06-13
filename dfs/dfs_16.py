"""
백준 - 욕심쟁이 판다
"""


import sys

sys.setrecursionlimit(10**6)


def dfs(n, x, y):
    dp[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if board[nx][ny] <= board[x][y]:
            continue

        if dp[nx][ny]:
            dp[x][y] = max(dp[x][y], dp[nx][ny] + 1)
            continue

        dp[x][y] = max(dp[x][y], dfs(n, nx, ny) + 1)

    return dp[x][y]


def solution(n):
    max_cnt = 0
    for i in range(n):
        for j in range(n):
            if not dp[i][j]:
                max_cnt = max(max_cnt, dfs(n, i, j))

    return max_cnt


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0] * n for _ in range(n)]

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    print(solution(n))
