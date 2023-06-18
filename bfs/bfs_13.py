"""
프로그래머스 - 리코쳇 로봇
"""


from collections import deque


def solution(board):

    q = deque([])
    visited = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'R':
                q.append((i, j, 0))
                break
        if q:
            break

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    while q:
        x, y, cnt = q.popleft()

        visited[x][y] = 1

        if board[x][y] == 'G':
            return cnt

        for i in range(4):

            m = 1
            while True:
                nx = x + dx[i] * m
                ny = y + dy[i] * m

                prev_nx = nx - dx[i]
                prev_ny = ny - dy[i]

                if nx < 0 or nx >= len(board) or ny < 0 or ny >= len(board[0]):
                    if not visited[prev_nx][prev_ny]:
                        q.append((prev_nx, prev_ny, cnt + 1))
                    break

                if board[nx][ny] == 'D':
                    if not visited[prev_nx][prev_ny]:
                        q.append((prev_nx, prev_ny, cnt + 1))
                    break

                m += 1

    return -1


if __name__ == "__main__":
    board = [".D.R", "....", ".G..", "...D"]
    print(solution(board))
    