"""
백준 - 텀 프로젝트
"""


import sys

sys.setrecursionlimit(10**6)


def dfs(dp, students, i, nth):

    if dp[i][0] == 2:
        return

    if dp[i][0] == 1 and dp[i][1] != nth:
        return

    dp[i] = dp[i][0] + 1, nth

    dfs(dp, students, students[i], nth)


def solution(n, students, dp):

    nth = 1
    for i in range(1, n + 1):
        if not dp[i][0]:
            dfs(dp, students, i, nth)
            nth += 1

    return sum([1 for i in range(1, n + 1) if dp[i][0] != 2])


if __name__ == "__main__":

    t = int(input())

    answer = []
    for _ in range(t):
        n = int(input())
        students = [0] + list(map(int, input().split()))
        dp = [(0, 0)] * (n + 1)
        answer.append(solution(n, students, dp))

    for a in answer:
        print(a)
