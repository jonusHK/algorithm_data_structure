import sys


def solution():
    """
    초기에 변의 길이가 1인 정삼각형을 두고, 그 변을 따라 나선 방향으로 정삼각형을 계속 추가한다.
    ex. 1 1 1 2 2 3 4 5 7 9 12 16 21 28 37 ...
    n 번째의 변의 길이를 구하는 프로그램
    """
    n = int(sys.stdin.readline())

    dp = [0 for _ in range(n + 1)]

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1

    for v in range(4, n + 1):
        dp[v] = dp[v - 3] + dp[v - 2]

    return dp[n]


print(solution())
