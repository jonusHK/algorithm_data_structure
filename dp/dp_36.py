"""
백준 - 제곱수의 합
"""


from math import sqrt


def solution(n):
    dp = [i for i in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(1, int(sqrt(i)) + 1):
            dp[i] = min(dp[i], dp[i-j*j] + 1)

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
