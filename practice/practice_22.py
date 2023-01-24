n, s, m = map(int, input().split())
volumes = list(map(int, input().split()))

dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
dp[0][s] = 1

for i in range(n):
    for j in range(m + 1):
        if dp[i][j] != 1:
            continue
        if j - volumes[i] >= 0:
            dp[i+1][j - volumes[i]] = 1
        if j + volumes[i] <= m:
            dp[i+1][j + volumes[i]] = 1


result = -1
for j in range(m, -1, -1):
    if dp[n][j] == 1:
        result = j
        break

print(result)
