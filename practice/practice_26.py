n, m = map(int, input().split())
dp = [[int(v) for v in input()] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 or j == 0 or dp[i][j] == 0:
            continue

        diag, top, left = dp[i-1][j-1], dp[i-1][j], dp[i][j-1]
        dp[i][j] = min(diag, top, left) + 1

max_num = max([max(row) for row in dp])

print(max_num ** 2)
