"""
백준 - 가장 큰 정사각형
"""

n, m = map(int, input().split())
array = [[int(s) for s in input()] for _ in range(n)]

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if array[i-1][j-1] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

max_num = max([max(row) for row in dp])
print(max_num**2)
