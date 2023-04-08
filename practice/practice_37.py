cnt = 0


def reverse(numbers, idx, dp):
    if not dp[idx]:
        dp[idx] = int(str(numbers[idx])[::-1])
    return dp[idx]


def solution(numbers):
    global cnt

    numbers_len = len(numbers)
    dp = [0] * numbers_len

    for i in range(numbers_len - 1):
        for j in range(i + 1, numbers_len):
            if numbers[i] + reverse(numbers, j, dp) == numbers[j] + reverse(numbers, i, dp):
                cnt += 1

    return cnt % (1e9 + 7)


if __name__ == "__main__":
    numbers = [42, 97, 13, 24, 1, 76]
    print(solution(numbers))
