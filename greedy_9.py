"""
백준 - 등수 매기기
"""

import sys

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))

array.sort()

result = 0
for i in range(1, len(array) + 1):
    result += abs(i - array[i - 1])

print(result)
