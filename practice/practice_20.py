n = int(input())
array = list(map(int, input().split()))

dp = [1 for _ in range(n)]

for i in range(0, n):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
