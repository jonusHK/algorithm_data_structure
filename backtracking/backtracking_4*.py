"""
백준 - 2048
"""


import copy
from typing import List

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]


def rotate_90(_board: List[List[int]], _n: int):
    new_board = copy.deepcopy(_board)
    for i in range(_n):
        for j in range(_n):
            new_board[j][_n-i-1] = _board[i][j]
    return new_board


def convert(_row: List[int], _n: int):
    new_list = [i for i in _row if i]
    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    new_list = [i for i in new_list if i]
    return new_list + [0] * (n - len(new_list))


def dfs(_n: int, _board: List[List[int]], count: int):
    ret = max([max(row) for row in _board])
    if count == 0:
        return ret
    for _ in range(4):
        # 좌측으로만 슬라이드 한다고 가정
        new_board = [convert(row, _n) for row in _board]
        if new_board != _board:
            ret = max(ret, dfs(n, new_board, count-1))
        _board = rotate_90(_board, _n)
    return ret


print(dfs(n, board, 5))
