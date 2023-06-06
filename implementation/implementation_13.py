"""
프로그래머스 - 숫자의 표현
"""


def solution(n):
    cnt = 1

    for i in range(1, n // 2 + 1):
        ptr = i + 1
        while i < n:
            i += ptr
            ptr += 1

        if i == n:
            cnt += 1

    return cnt


if __name__ == "__main__":
    n = 15
    print(solution(n))
