"""
백준 - 1로 만들기
"""


def solution(num):

    for i in range(2, num + 1):
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)

        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)

        dp[i] = min(dp[i], dp[i-1] + 1)

    return dp[num]


if __name__ == "__main__":
    num = int(input())
    dp = [1e6] * (num + 1)
    dp[1] = 0
    print(solution(num))
