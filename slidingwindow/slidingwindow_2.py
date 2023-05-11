"""
백준 - 게으른 백곰
"""


def solution(arr, k, min_idx, max_idx):
    left = min_idx
    right = left + (k * 2)
    max_n = sum_n = sum(arr[left:right+1])

    while True:
        right += 1
        if right > max_idx:
            break

        sum_n += arr[right] - arr[left]
        max_n = max(max_n, sum_n)
        left += 1

    return max_n


if __name__ == "__main__":
    n, k = map(int, input().split())
    arr_len = 1000001
    arr = [0] * arr_len

    min_idx = arr_len
    max_idx = 0
    for i in range(n):
        g, x = map(int, input().split())
        arr[x] = g
        min_idx = min(min_idx, x)
        max_idx = max(max_idx, x)

    print(solution(arr, k, min_idx, max_idx))
