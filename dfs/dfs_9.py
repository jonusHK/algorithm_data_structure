"""
프로그래머스 - 퍼즐 조각 채우기
"""


from copy import deepcopy


def solution(game_board, table):
    answer = 0

    n = len(game_board)
    empty_boards = []

    for i in range(n):
        for j in range(n):
            if game_board[i][j] == 0:
                empty_boards.append(dfs(game_board, i, j, [0, 0], n, 0))

    for _ in range(4):
        table = rotate(table)
        copied_table = deepcopy(table)
        for i in range(n):
            for j in range(n):
                if copied_table[i][j] == 1:
                    block = dfs(copied_table, i, j, [0, 0], n, 1)
                    if block in empty_boards:
                        empty_boards.remove(block)
                        answer += len(block)
                        table = deepcopy(copied_table)
                    else:
                        copied_table = deepcopy(table)

    return answer


def dfs(board, x, y, position, n, flag):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    result = [position]

    # 방문 체크
    board[x][y] = 2

    for i in range(4):
        px = x + dx[i]
        py = y + dy[i]

        if 0 <= px < n and 0 <= py < n and board[px][py] == flag:
            result += dfs(board, px, py, [position[0] + dx[i], position[1] + dy[i]], n, flag)

    return result


def rotate(table):
    n = len(table)
    rotated = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1] = table[i][j]

    return rotated


if __name__ == "__main__":
    game_board = [[1,1,0,0,1,0], [0,0,1,0,1,0], [0,1,1,0,0,1], [1,1,0,1,1,1], [1,0,0,0,1,0], [0,1,1,1,0,0]]
    table = [[1,0,0,1,1,0], [1,0,1,0,1,0], [0,1,1,0,1,1], [0,0,1,0,0,0], [1,1,0,1,1,0], [0,1,0,0,0,0]]
    print(solution(game_board, table))
