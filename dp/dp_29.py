"""
백준 - 동전2
"""


def solution():
    dp = [1e9] * 10001
    dp[0] = 0

    for i in range(1, k + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[k] if dp[k] < 1e9 else -1


if __name__ == "__main__":
    # 1 <= n <= 100
    # 1 <= k <= 10,000
    # 1 <= 동전 가치 <= 100,000
    n, k = map(int, input().split())
    coins = [int(input()) for _ in range(n)]
    coins.sort(reverse=True)
    print(solution())
