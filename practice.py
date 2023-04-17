"""
백준 - 2xn 타일링
"""


def solution(n):
    dp = [0] * 1001

    for i in range(1, len(dp)):
        if i in (1, 2):
            dp[i] = i
            continue

        dp[i] = (dp[i-1] + dp[i-2]) % 10007
        if i == n:
            return dp[i]


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
