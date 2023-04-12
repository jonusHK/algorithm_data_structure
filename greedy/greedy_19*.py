"""
프로그래머스 - 인사고과
"""


def solution(scores):
    target = scores[0]
    target_sum = sum(target)
    scores.sort(key=lambda x: (-x[0], x[1]))

    std = 0
    order = 1
    for score in scores:
        if std <= score[1]:
            if target_sum < sum(score):
                order += 1
            std = score[1]
        elif score == target:
            return -1

    return order


if __name__ == "__main__":
    scores = [[2, 2], [1, 4], [3, 2], [3, 2], [2, 1]]
    print(solution(scores))
