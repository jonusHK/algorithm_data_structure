"""
백준 - The candy war
"""


def is_same(_c):
    return len(set(_c)) == 1


def teacher(_c):
    for i, v in enumerate(_c):
        if v % 2 == 1:
            _c[i] += 1
    return _c


def get_count_until_same(_n, _c):
    cnt = 0
    len_c = len(_c)
    plus = [0] * len_c

    teacher(_c)

    while not is_same(_c):
        for i, v in enumerate(_c):
            assert v % 2 == 0, 'Should be even.'
            _c[i] = _c[i] // 2
            plus[(i+1) % _n] = _c[i]

        for i in range(len_c):
            _c[i] += plus[i]
            plus[i] = 0

        teacher(_c)
        cnt += 1

    return cnt


array = []
t = int(input())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    array.append(get_count_until_same(n, c))

[print(v) for v in array]
