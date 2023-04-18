import random
import string


def solution(N):
    s = set()

    # N이 표현 가능한 문자열 길이보다 같거나 짧은 경우
    if N <= len(string.ascii_lowercase):
        while len(s) < N:
            s.add(random.choice(string.ascii_lowercase))

        return ''.join(s)

    # N이 표현 가능한 문자열 길이보다 긴 경우
    cnt = 2
    while N % cnt != 0:
        cnt += 1

    while len(s) < N // cnt:
        s.add(random.choice(string.ascii_lowercase))

    return ''.join(s) * cnt


if __name__ == "__main__":
    N = 28
    print(solution(N))
