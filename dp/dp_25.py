"""
프로그래머스 - 타겟 넘버 (동적계획법 풀이)
"""


def solution(numbers, target):
    dp = [[] for _ in range(len(numbers))]
    dp[0] = [numbers[0], -numbers[0]]

    for i in range(1, len(numbers)):
        for v in dp[i-1]:
            dp[i].append(v + numbers[i])
            dp[i].append(v - numbers[i])

    return sum([1 for v in dp[-1] if v == target])


if __name__ == "__main__":
    numbers = [4, 1, 2, 1]
    target = 4
    print(solution(numbers, target))
