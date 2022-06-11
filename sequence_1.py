"""
백준 - 수빈이와 수열
"""

n = int(input())
b = list(map(int, input().split()))

for i in range(n):
    print(b[i] * (i + 1) - b[i - 1] * i, end=' ')
