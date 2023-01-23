from copy import deepcopy
from typing import Tuple, List

n, m, k = map(int, input().split())
array = []
rotate_rule = []
for _ in range(n):
    row = list(map(int, input().split()))
    array.append(row)

for _ in range(k):
    rule = tuple(map(int, input().split()))
    rotate_rule.append(rule)


def rotate(arr: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]):
    top, bottom, left, right = start[0], end[0], start[1], end[1]
    if top == bottom:
        return

    temp = arr[top][left]
    # 맨 왼쪽 하 -> 상
    for i in range(top, bottom):
        arr[i][left] = arr[i+1][left]
    # 맨 아래쪽 우 -> 좌
    for j in range(left, right):
        arr[bottom][j] = arr[bottom][j+1]
    # 맨 오른쪽 상 -> 하
    for i in range(bottom, top, -1):
        arr[i][right] = arr[i-1][right]
    # 맨 위쪽 좌 -> 우
    for j in range(right, left, -1):
        arr[top][j] = arr[top][j-1]

    arr[top][left+1] = temp
    rotate(arr, (top + 1, left + 1), (bottom - 1, right - 1))


def dfs(arr: List[List[int]]):
    global min_value

    if len(list(filter(lambda x: x is True, checked))) == k:
        min_value = min(min([sum(arr[i]) for i in range(n)]), min_value)
        return

    for i, (r, c, s) in enumerate(rotate_rule):
        if checked[i]:
            continue
        checked[i] = True
        st, ed = (r - s - 1, c - s - 1), (r + s - 1, c + s - 1)
        copied_arr = deepcopy(arr)
        rotate(copied_arr, st, ed)
        dfs(copied_arr)
        checked[i] = False


min_value = 100 * 50 * 50
checked = [False for _ in range(k)]
dfs(array)

print(min_value)
