import sys
from collections import deque
from itertools import combinations
from copy import deepcopy


def get_new_board(n, m, board):
    new_board = [[1 for _ in range(m + 2)] for _ in range(n + 2)]

    for i in range(n):
        for j in range(m):
            new_board[i+1][j+1] = board[i][j]
    
    return new_board


def set_virus_to_board(n, m, board, wall_pos_case):
    board = deepcopy(board)
    q = deque()
    visited = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 2:
                q.append((i, j))
                visited.append((i, j))
    
    while q:
        pos = q.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        for i in range(4):
            x = pos[0] + dx[i]
            y = pos[1] + dy[i]

            if board[x][y] == 0:
                if (x, y) not in visited and (x, y) not in wall_pos_case:
                    board[x][y] = 2
                    q.append((x, y))
                    visited.append((x, y))

    return board
        

def get_safty_pos_case(n, m ,board):
    safty_pos_case = []
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                safty_pos_case.append((i, j))

    return safty_pos_case


def find_safty_cnt(n, m, board):
    cnt = -3
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt += 1

    return cnt if cnt > 0 else 0

def solution():
    """
    7 7
    2 0 0 0 1 1 0
    0 0 1 0 1 2 0
    0 1 1 0 1 0 0
    0 1 0 0 0 0 0
    0 0 0 0 0 1 1
    0 1 0 0 0 0 0
    0 1 0 0 0 0 0
    """
    n, m = map(int, sys.stdin.readline().split())

    board = []
    for _ in range(n):
        board.append(list(map(int, sys.stdin.readline().split())))

    new_board = get_new_board(n, m, board)
    new_n = n + 2
    new_m = m + 2

    safty_pos_case = get_safty_pos_case(new_n, new_m, new_board)

    max_cnt = 0
    wall_pos_case_li = list(combinations(safty_pos_case, 3))
    for wall_pos_case in wall_pos_case_li:
        virus_board = set_virus_to_board(new_n, new_m, new_board, wall_pos_case)
        cnt = find_safty_cnt(new_n, new_m, virus_board)
        
        max_cnt = max(max_cnt, cnt)

    return max_cnt


print(solution())
