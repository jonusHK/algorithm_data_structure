"""
프로그래머스 - 테이블 해시 함수
"""


def generate_s_i(li, i):
    rst = 0
    for v in li:
        rst += v % i

    return rst


def solution(data, col, row_begin, row_end):
    data.sort(key=lambda x: (x[col-1], -x[0]))

    rst = 0
    for i in range(row_begin, row_end + 1):
        rst ^= generate_s_i(data[i-1], i)

    return rst


if __name__ == "__main__":
    data = [[2,2,6],[1,5,10],[4,2,9],[3,8,3]]
    col = 2
    row_begin = 2
    row_end = 3
    print(solution(data, col, row_begin, row_end))
