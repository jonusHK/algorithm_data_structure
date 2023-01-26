n = int(input())
array = [(0, 0, 0, 0)]
for i in range(1, n + 1):
    a, h, w = map(int, input().split())
    array.append((a, h, w, i))

array.sort()

dp = [0] * (n + 1)

visited = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i - 1, -1, -1):
        if array[j][2] < array[i][2]:
            dp[i] = max(dp[i], dp[j] + array[i][1])

max_value = max(dp)
index = n

results = []
while index != 0:
    if max_value == dp[index]:
        results.append(array[index][3])
        max_value -= array[index][1]
    index -= 1

length = len(results)
print(length)
for i in range(length - 1, -1, -1):
    print(results[i])
