"""
프로그래머스 - 카운트다운
"""


from collections import deque

MAX_SCORE = 20
CENTER_SCORE = 50


def solution(target):
    dp = [[1e9, -1] for _ in range(target + 1)]
    q = deque([(0, 0, 0)])

    while q:
        score, dart, single_center = q.popleft()

        # 싱글, 더블, 트리플 점수 처리
        for i in range(1, MAX_SCORE + 1):
            for j in range(1, 4):
                _score = i * j + score
                if _score > target:
                    continue

                _single_center = single_center + 1 if j == 1 else single_center
                if dp[_score][0] >= dart + 1 and dp[_score][1] < _single_center:
                    dp[_score] = [dart + 1, _single_center]
                    q.append((_score, dart + 1, _single_center))

        # 불 점수 처리
        if score + CENTER_SCORE > target:
            continue

        if dp[score+CENTER_SCORE][0] >= dart + 1 and dp[score+CENTER_SCORE][1] < single_center + 1:
            dp[score+CENTER_SCORE] = [dart + 1, single_center + 1]
            q.append((score + CENTER_SCORE, dart + 1, single_center + 1))

    return dp[-1]


if __name__ == "__main__":
    target = 58
    print(solution(target))
