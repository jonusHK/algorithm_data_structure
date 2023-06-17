"""
백준 - 점프
"""


def is_arrived(x, y):
    return x == n - 1 and y == n - 1


def dfs(x, y):

    if is_arrived(x, y):
        return 1

    if dp[x][y]:
        return dp[x][y]

    for i in range(2):
        nx = x + dx[i] * board[x][y]
        ny = y + dy[i] * board[x][y]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if not board[nx][ny] and not is_arrived(nx, ny):
            continue

        dp[x][y] += dfs(nx, ny)

    return dp[x][y]


def solution():
    return dfs(0, 0)


if __name__ == "__main__":
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * n for _ in range(n)]
    dx, dy = [0, 1], [1, 0]

    print(solution())
