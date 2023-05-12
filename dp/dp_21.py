"""
백준 - 설탕 배달
"""


def solution(n):
    dp = [-1] * 5001

    a = 3
    b = 5

    dp[a] = 1
    dp[b] = 1

    for i in range(a, len(dp)):
        if dp[i-a] >= 1:
            dp[i] = dp[i-a] + 1

        if dp[i-b] >= 1:
            dp[i] = min(dp[i-b] + 1, dp[i]) if dp[i] != -1 else dp[i-b] + 1

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
