"""
백준 - 쉬운 계단 수
"""


def solution(n):

    dp = [[0] * 10 for _ in range(n + 1)]

    for i in range(1, 10):
        dp[1][i] = 1

    for i in range(2, n + 1):
        dp[i][0] = dp[i-1][1]
        dp[i][9] = dp[i-1][8]

        for j in range(1, 9):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

    return sum(dp[n]) % int(1e9)


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
