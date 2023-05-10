def solution():
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    left = 0
    right = 1

    rst = arr[left]
    cnt = 0

    while left < n:
        if rst < m:
            if right >= n:
                break
            rst += arr[right]
            right += 1
        elif rst == m:
            cnt += 1
            rst -= arr[left]
            left += 1
        else:
            rst -= arr[left]
            left += 1

    return cnt


if __name__ == "__main__":
    print(solution())
