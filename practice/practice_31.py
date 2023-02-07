n = int(input())

board = [[0] * n for _ in range(n)]
case_cnt = 0

dx = [-1, 1, 1, -1]
dy = [1, 1, -1, -1]


def is_possible(x: int, y: int):
    for i in range(n):
        if board[i][y] == 1 or board[x][i] == 1:
            return False

        for j in range(4):
            _x, _y = dx[j] * i, dy[j] * i
            __x, __y = x + _x, y + _y
            if 0 <= __x < n and 0 <= __y < n:
                if board[__x][__y] == 1:
                    return False
    return True


def backtracking(row: int):
    global case_cnt

    if row == n:
        case_cnt += 1
        return

    for col in range(n):
        if is_possible(row, col):
            board[row][col] = 1
            backtracking(row + 1)
            if case_cnt > 0:
                return
            board[row][col] = 0


backtracking(0)

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            print(j + 1)
            break
