"""
백준 - 연속합
"""


def solution(n):
    for i in range(1, n):
        dp[i] = max(dp[i], dp[i-1] + dp[i])

    return max(dp)


if __name__ == "__main__":
    n = int(input())
    dp = list(map(int, input().split()))
    print(solution(n))
