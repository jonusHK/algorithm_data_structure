from typing import List


def calculate_min_sum(n: int, sa: List[int]):
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(1, n - i + 2):
            dp[j][j+i-1] = min([
                dp[j][j+m] + dp[j+m+1][j+i-1] for m in range(i - 1)
            ]) + sa[j+i-1] - sa[j-1]

    print(dp[1][n])


t = int(input())
for _ in range(t):
    k = int(input())
    array = list(map(int, input().split()))
    sum_array = [0] * (k + 1)
    for idx in range(1, k + 1):
        sum_array[idx] = sum_array[idx-1] + array[idx-1]
    calculate_min_sum(k, sum_array)
