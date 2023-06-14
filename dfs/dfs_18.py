"""
백준 - 트리의 지름
"""


import sys

sys.setrecursionlimit(10**6)


def dfs(node):

    visited[node] = 1

    for n, d in tree[node]:
        if visited[n]:
            continue

        if dp[n][0]:
            if dp[node][0] < dp[n][0] + d:
                dp[node] = dp[n][0] + d, dp[n][1]
            continue

        max_d, max_n = dfs(n)
        if dp[node][0] < max_d + d:
            dp[node] = max_d + d, max_n

    visited[node] = 0

    return dp[node]


def init_dp():
    global dp

    dp = [(0, i) for i in range(v + 1)]
    return dp


def solution():
    cnt, node = dfs(1)
    init_dp()
    return dfs(node)[0]


if __name__ == "__main__":
    v = int(input())

    tree = [[] for _ in range(v + 1)]
    for _ in range(v):
        row = list(map(int, input().split()))
        for i in range(1, len(row) - 1, 2):
            tree[row[0]].append((row[i], row[i+1]))

    dp = init_dp()
    visited = [0] * (v + 1)

    print(solution())
