"""
백준 - 앱
"""


def solution(N, M, arr_m, arr_c):

    dp = [[0 for _ in range(sum(arr_c) + 1)] for _ in range(N + 1)]
    result = sum(arr_c)

    for i in range(1, N + 1):
        byte = arr_m[i]
        cost = arr_c[i]

        for j in range(1, sum(arr_c) + 1):
            if j < cost:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(byte + dp[i-1][j-cost], dp[i-1][j])

            if dp[i][j] >= M:
                result = min(result, j)

    return result


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr_m = [0] + list(map(int, input().split()))
    arr_c = [0] + list(map(int, input().split()))
    print(solution(N, M, arr_m, arr_c))
