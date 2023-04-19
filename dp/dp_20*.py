"""
프로그래머스 - 억억단을 외우자
"""


def solution(e, starts):
    arr = [0] * (e + 1)
    for n in range(1, int(e ** 0.5) + 1):
        arr[n*n] += 1
        for i in range(n * (n + 1), e + 1, n):
            arr[i] += 2

    sorted_starts = sorted(starts)

    rst = []
    answer = {}
    max_idx = 0
    for i, n in enumerate(sorted_starts):
        if not max_idx or max_idx < n:
            max_idx = arr[n:].index(max(arr[n:])) + n
        answer[n] = max_idx

    for n in starts:
        rst.append(answer[n])

    return rst


if __name__ == "__main__":
    e = 8
    starts = [1, 3, 7]
    print(solution(e, starts))
