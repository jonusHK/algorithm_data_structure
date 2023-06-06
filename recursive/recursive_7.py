"""
프로그래머스 - 하노이의 탑
"""


def move(start, end):
    return [start, end]


def hanoi(n, start, end, sub, answer):
    if n == 1:
        answer.append(move(start, end))
        return
    
    hanoi(n - 1, start, sub, end, answer)
    answer.append(move(start, end))
    hanoi(n - 1, sub, end, start, answer)


def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)

    return answer


if __name__ == "__main__":
    n = 5
    print(solution(n))
