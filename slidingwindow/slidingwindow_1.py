"""
백준 - 수열
"""


def solution(arr, n, k):
    left = 0
    right = k - 1

    sum_num = sum(arr[:k])
    max_num = max(-100 * n, sum_num)

    while True:
        right += 1
        if right == n:
            break

        sum_num += arr[right] - arr[left]
        max_num = max(max_num, sum_num)
        left += 1

    return max_num


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(solution(arr, n, k))
