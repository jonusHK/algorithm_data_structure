"""
프로그래머스 - 요격 시스템
"""


def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))

    cnt = p = 0
    for t in targets:
        if t[0] >= p:
            cnt += 1
            p = t[1]

    return cnt


if __name__ == "__main__":
    targets = [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]
    print(solution(targets))
    