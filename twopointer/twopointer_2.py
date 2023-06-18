"""
프로그래머스 - 연속된 부분 수열의 합
"""


def solution(sequence, k):
    n = len(sequence)

    _sum = 0
    end = 0
    length = n + 1
    res = []
    for start in range(n):
        while _sum < k and end < n:
            _sum += sequence[end]
            end += 1

        if _sum == k and end - start < length:
            res = [start, end - 1]
            length = end - start

        _sum -= sequence[start]

    return res


if __name__ == "__main__":
    sequence = [1, 2, 3, 4, 5]
    k = 7
    print(solution(sequence, k))
