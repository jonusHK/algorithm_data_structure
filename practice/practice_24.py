from typing import List

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

shift_cnt = 5
max_num = 0


def rotate_90(_board: List[List[int]]):
    rotated_board = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated_board[j][n-i-1] = _board[i][j]
    return rotated_board


def shift_left(_row: List[int]):
    _row = [v for v in _row if v]
    for i in range(1, len(_row)):
        if _row[i-1] == _row[i]:
            _row[i-1] *= 2
            _row[i] = 0
    _row = [v for v in _row if v]
    return _row + [0] * (n - len(_row))


def find_max(_board: List[List[int]]):
    global max_num
    for i in range(n):
        max_num = max(max_num, max(_board[i]))


def dfs(_board: List[List[int]]):
    global shift_cnt

    if shift_cnt == 0:
        find_max(_board)
        return

    for i in range(4):
        shifted_board = [shift_left(row) for row in _board]
        shift_cnt -= 1
        dfs(shifted_board)
        _board = rotate_90(_board)
        shift_cnt += 1


dfs(board)
print(max_num)
