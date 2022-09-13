"""
백준 - 배열 돌리기 4
"""
import copy
from typing import Tuple, List

n, m, k = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(n)]
rotate_case = [list(map(int, input().split())) for _ in range(k)]


def rotate(arr: List[List[int]], lt: Tuple[int, int], rb: Tuple[int, int]) -> None:
    # lt: 맨 왼쪽 위 좌표, rb: 맨 오른쪽 아래 좌표
    top, bottom, left, right = lt[0], rb[0], lt[1], rb[1]
    if top == bottom:
        return

    temp = arr[top][left]
    # 맨 왼쪽 아래 -> 위
    for i in range(top, bottom):
        arr[i][left] = arr[i+1][left]
    # 맨 아래쪽 우 -> 좌
    for i in range(left, right):
        arr[bottom][i] = arr[bottom][i+1]
    # 맨 오른쪽 위 -> 아래
    for i in range(bottom, top, -1):
        arr[i][right] = arr[i-1][right]
    # 맨 위쪽 좌 -> 우
    for i in range(right, left, -1):
        arr[top][i] = arr[top][i-1]

    arr[top][left+1] = temp
    next_lt, next_rb = (top + 1, left + 1), (bottom - 1, right - 1)
    rotate(arr, next_lt, next_rb)


def get_min_value(li: List[List[int]]) -> int:
    return min([sum(i) for i in li])


def dst(arr: List[List[int]], checked: List[int]) -> None:
    global min_value
    if sum(checked) == k:
        min_value = min(min_value, get_min_value(arr))
        return

    for i in range(k):
        if checked[i]:
            continue
        checked[i] = 1
        new_arr = copy.deepcopy(arr)
        r, c, s = rotate_case[i]
        rotate(new_arr, (r - s - 1, c - s - 1), (r + s - 1, c + s - 1))
        dst(new_arr, checked)
        checked[i] = 0


min_value = 10000
dst(array, [0 for _ in range(k)])
print(min_value)
