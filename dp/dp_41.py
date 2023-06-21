"""
백준 - 내려가기
"""


if __name__ == "__main__":
    n = int(input())

    max_dp = [0, 0, 0]
    min_dp = [0, 0, 0]

    for i in range(n):
        arr = list(map(int, input().split()))

        if i == 0:
            max_dp = arr
            min_dp = arr
            continue

        max_dp = [arr[0] + max(max_dp[0], max_dp[1]), arr[1] + max(max_dp), arr[2] + max(max_dp[1], max_dp[2])]
        min_dp = [arr[0] + min(min_dp[0], min_dp[1]), arr[1] + min(min_dp), arr[2] + min(min_dp[1], min_dp[2])]

    print(max(max_dp), min(min_dp))
