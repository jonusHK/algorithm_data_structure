"""
백준 - 설탕 배달
"""


def solution(n):

    for i in range(n // 5, -1, -1):
        for j in range(n // 3 + 1):
            if 5 * i + 3 * j == n:
                return i + j

    return -1


if __name__ == "__main__":
    n = int(input())
    print(solution(n))
