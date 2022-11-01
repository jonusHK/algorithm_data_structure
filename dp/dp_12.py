"""
백준 - 가장 큰 증가 부분 수열
"""
from copy import deepcopy

n = int(input())
array = list(map(int, input().split()))
dp = deepcopy(array)

for i in range(1, n):
    for j in range(i):
        if array[i] > array[j]:
            dp[i] = max((array[i] + dp[j]), dp[i])

print(max(dp))
