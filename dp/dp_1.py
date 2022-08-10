import sys


def solution():
    """
    2 * n 타일에 2 * 1 혹은 1 * 2 채우는 경우의 수
    """
    n = int(sys.stdin.readline())

    # 빈 리스트 추출
    dp = [0 for _ in range(n + 1)]

    # 초기값 설정
    dp[1] = 1
    dp[2] = 2

    for v in range(3, n + 1):
        # 점화식 계산
        dp[v] = dp[v - 1] + dp[v - 2]

    return dp[n]

print(solution())
