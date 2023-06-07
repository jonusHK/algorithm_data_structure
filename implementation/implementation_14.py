"""
프로그래머스 - 두 원 사이의 정수 쌍
"""


from math import sqrt


def solution(r1, r2):

    r1_cnt = r2_cnt = r1_edge_cnt = 0

    for x in range(1, r2):
        if x < r1:
            y = sqrt(r1 ** 2 - x ** 2)
            r1_cnt += int(y)

            if y % 1 == 0:
                r1_edge_cnt += 1

        r2_cnt += int(sqrt(r2 ** 2 - x ** 2))

    return (r2_cnt - r1_cnt + r1_edge_cnt + r2 - r1 + 1) * 4


if __name__ == "__main__":
    r1, r2 = 2, 3
    print(solution(r1, r2))
