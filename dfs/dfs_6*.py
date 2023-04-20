"""
프로그래머스 - 숫자 타자 대회
"""

import math
import sys

sys.setrecursionlimit(200_000)

weights = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],  # 0
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],  # 1
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],  # 2
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],  # 3
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],  # 4
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],  # 5
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],  # 6
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],  # 7
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],  # 8
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],  # 9
]

dp = [
    [[0] * 10 for _ in range(10)]
    for _ in range(100_001)
]


def solve(numbers, left, right, ptr=0):
    if ptr == len(numbers):
        return 0

    if dp[ptr][left][right]:
        return dp[ptr][left][right]

    num = numbers[ptr]
    w = math.inf

    if num != right:
        w = min(w, solve(numbers, num, right, ptr + 1) + weights[left][num])

    if num != left:
        w = min(w, solve(numbers, left, num, ptr + 1) + weights[right][num])

    dp[ptr][left][right] = dp[ptr][right][left] = w

    return w


def solution(numbers):
    return solve([int(n) for n in numbers], 4, 6)


if __name__ == "__main__":
    numbers = "8123"
    print(solution(numbers))
