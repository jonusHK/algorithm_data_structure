"""
프로그래머스 - 타겟 넘버 (BFS 풀이)
"""


from collections import deque


def solution(numbers, target):
    cnt = 0
    q = deque([(0, 0, '+'), (0, 0, '-')])

    while q:
        idx, calc, sign = q.popleft()

        if sign == '+':
            calc += numbers[idx]
        else:
            calc -= numbers[idx]

        if idx == len(numbers) - 1:
            if calc == target:
                cnt += 1
            continue

        for sign in ['+', '-']:
            q.append((idx + 1, calc, sign))

    return cnt


if __name__ == "__main__":
    numbers = [4, 1, 2, 1]
    target = 4
    print(solution(numbers, target))
