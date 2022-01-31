import sys


def binary_search(li, num, st, ed):
    if st > ed:
        return 0

    mid = (st + ed) // 2
    mid_num = li[mid]

    if num == mid_num:
        return 1

    elif num > mid_num:
        return binary_search(li, num, mid + 1, ed)

    else:
        return binary_search(li, num, st, mid - 1)

def solution():
    n = int(sys.stdin.readline())
    n_li = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    m_li = list(map(int, sys.stdin.readline().split()))

    n_li.sort()
    for m_num in m_li:
        print(binary_search(n_li, m_num, 0, n - 1))

solution()
