"""
백준 - 수 찾기
"""

n = int(input())
n_li = list(map(int, input().split()))
m = int(input())
m_li = list(map(int, input().split()))


def binary_search(v: int, st: int, ed: int):
    if st > ed:
        return 0

    mid = (st + ed) // 2
    if v == n_li[mid]:
        return 1

    return binary_search(v, mid + 1, ed) if v > n_li[mid] else binary_search(v, st, mid - 1)


n_li.sort()

for num in m_li:
    print(binary_search(num, 0, n - 1))
