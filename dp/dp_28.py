"""
백준 - 피보나치 함수
"""


def solution(num):
    dp = [(0, 0)] * (num + 1)
    dp[0] = (1, 0)

    if num == 0:
        return dp[0]

    dp[1] = (0, 1)

    for i in range(2, num + 1):
        dp[i] = (dp[i-2][0] + dp[i-1][0], dp[i-2][1] + dp[i-1][1])

    return dp[num]


if __name__ == "__main__":
    answer = []
    for _ in range(int(input())):
        answer.append(solution(int(input())))

    for a in answer:
        print(a[0], a[1])
