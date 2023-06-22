"""
백준 - 1, 2, 3 더하기 3
"""


def solution(n):

    if n in (0, 1, 2):
        return n

    dp = [0] * (n + 1)

    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % 1000000009

    return dp[n]


if __name__ == "__main__":

    answer = []
    for _ in range(int(input())):
        n = int(input())
        answer.append(solution(n))

    for a in answer:
        print(a)
