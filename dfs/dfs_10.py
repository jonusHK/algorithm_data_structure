"""
프로그래머스 - 타겟 넘버 (DFS 풀이)
"""


def dfs(numbers, target, idx, calc):
    cnt = 0

    if idx == len(numbers) - 1:
        return 1 if calc == target else 0

    for sign in ('+', '-'):
        _calc = calc + numbers[idx+1] if sign == '+' else calc - numbers[idx+1]
        cnt += dfs(numbers, target, idx + 1, _calc)

    return cnt


def solution(numbers, target):
    return dfs(numbers, target, 0, numbers[0]) + dfs(numbers, target, 0, -numbers[0])


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    target = 3
    print(solution(numbers, target))
