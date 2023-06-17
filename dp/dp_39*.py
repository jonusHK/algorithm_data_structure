"""
백준 - 팰린드롬? (다른 풀이로 풀어 볼 것)
"""


def is_symmetric(s, e):
    if s == e:
        return True

    mid = (s + e) // 2
    for i in range(e, mid - 1, -1):
        if arr[i] != arr[s+e-i]:
            return False

    return True


def handle_symmetric(s, e):
    while s <= e:
        dp[s][e] = 1
        s += 1
        e -= 1


def init_dp():
    global dp

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            if dp[i][j]:
                continue

            if is_symmetric(i, j):
                handle_symmetric(i, j)


def solution(s, e):
    return dp[s][e]


if __name__ == "__main__":
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    init_dp()

    answer = []
    m = int(input())
    for _ in range(m):
        s, e = map(int, input().split())
        answer.append(solution(s, e))

    for a in answer:
        print(a)
