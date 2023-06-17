"""
프로그래머스 - 가장 긴 팰린드롬
"""


def solution(s):
    n = len(s)

    max_cnt = 1
    dp = [[0] * n for _ in range(n)]

    for i in range(1, n):
        dp[i][i] = 1

        if i < n - 1 and s[i] == s[i+1]:
            dp[i][i+1] = 1

    for i in range(3, n + 1):
        for j in range(n - i + 1):
            if s[j] == s[j+i-1] and dp[j+1][j+i-2]:
                dp[j][j+i-1] = 1
                max_cnt = max(max_cnt, i)

    return max_cnt


if __name__ == "__main__":
    s = "a"
    print(solution(s))
