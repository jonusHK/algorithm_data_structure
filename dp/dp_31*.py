"""
백준 - 외판원 순회
"""


def dfs(city, visited):

    # 모두 방문한 경우
    if visited == (1 << n) - 1:
        return w[city][0] or INF

    if dp[city][visited]:
        return dp[city][visited]

    tmp = INF
    for i in range(1, n):
        if not w[city][i]:
            continue

        if visited & (1 << i):
            continue

        tmp = min(tmp, w[city][i] + dfs(i, visited | (1 << i)))

    dp[city][visited] = tmp

    return dp[city][visited]


def solution():
    return dfs(0, 1 << 0)


if __name__ == "__main__":
    n = int(input())
    w = [list(map(int, input().split())) for _ in range(n)]

    dp = [[0] * (1 << n) for _ in range(n)]
    INF = float('inf')
    print(solution())
