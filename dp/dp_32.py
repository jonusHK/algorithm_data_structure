"""
백준 - 포도주 시식
"""


def solution(n):
    dp[1] = arr[1]

    for i in range(2, n + 1):
        if i == 2:
            dp[i] = arr[1] + arr[2]
        else:
            dp[i] = max(dp[i-1], dp[i-2] + arr[i], dp[i-3] + arr[i-1] + arr[i])

    return dp[-1]


if __name__ == "__main__":
    n = int(input())
    arr = [0] + [int(input()) for _ in range(n)]
    dp = [0] * (n + 1)
    print(solution(n))
