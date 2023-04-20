import random
import string


def solution(N):

    # N이 표현 가능한 문자열 길이보다 같거나 짧은 경우
    if N <= len(string.ascii_lowercase):
        return ''.join(random.sample(string.ascii_lowercase, N))

    # N이 표현 가능한 문자열 길이보다 긴 경우
    cnt = 2
    while N % cnt != 0:
        cnt += 1

    return ''.join(random.sample(string.ascii_lowercase, N // cnt) * cnt)


if __name__ == "__main__":
    N = 28
    print(solution(N))
