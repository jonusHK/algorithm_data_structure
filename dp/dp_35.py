"""
백준 - 이항 계수 2
"""


def solution(n, k):

    dp = [1] * (n + 1)

    for i in range(1, n + 1):
        dp[i] = dp[i-1] * i

    return dp[n] // (dp[k] * dp[n-k]) % 10007


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(solution(n, k))
