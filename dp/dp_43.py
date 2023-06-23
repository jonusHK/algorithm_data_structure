"""
백준 - LCS 2
"""


def solution(u, v):

    dp = [[0] * (len(v) + 1) for _ in range(len(u) + 1)]

    for i in range(1, len(u) + 1):
        for j in range(1, len(v) + 1):
            if v[j-1] == u[i-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    rst = []

    i, j = len(u), len(v)
    while i > 0 and j > 0:

        if dp[i][j] == dp[i][j-1]:
            j -= 1
            continue

        if dp[i][j] != dp[i-1][j]:
            rst.append(u[i-1])
            j -= 1

        i -= 1

    return ''.join(rst[::-1]) if rst else ''


if __name__ == "__main__":
    u = input()
    v = input()
    lcs = solution(u, v)

    print(len(lcs))
    if lcs:
        print(lcs)
