"""
백준 - 두 동전
"""

from collections import deque


def convert_to_idx(x, y):
    return int(str(x) + str(y))


def in_board(x, y):
    return 0 <= x < n and 0 <= y < m


def bfs(pos1, pos2):
    visited = [[0] * 2000 for _ in range(2000)]
    visited[convert_to_idx(pos1[0], pos1[1])][convert_to_idx(pos2[0], pos2[1])] = 1
    q = deque([(pos1[0], pos1[1], pos2[0], pos2[1], 0)])

    while q:
        x1, y1, x2, y2, cnt = q.popleft()

        if cnt == 10:
            return -1

        for i in range(4):
            nx1 = x1 + dx[i]
            ny1 = y1 + dy[i]
            nx2 = x2 + dx[i]
            ny2 = y2 + dy[i]

            if in_board(nx1, ny1) and in_board(nx2, ny2):
                if board[nx1][ny1] == '#' and board[nx2][ny2] == '#':
                    continue

                if board[nx1][ny1] == '#':
                    nx1, ny1 = x1, y1

                if board[nx2][ny2] == '#':
                    nx2, ny2 = x2, y2

                x_idx = convert_to_idx(nx1, ny1)
                y_idx = convert_to_idx(nx2, ny2)

                if not visited[x_idx][y_idx]:
                    q.append((nx1, ny1, nx2, ny2, cnt + 1))
                    visited[x_idx][y_idx] = 1

            elif not in_board(nx1, ny1) and not in_board(nx2, ny2):
                continue

            else:
                return cnt + 1

    return -1


def solution():
    coin_pos = []

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'o':
                coin_pos.append((i, j))

    return bfs(coin_pos[0], coin_pos[1])


if __name__ == "__main__":
    # N : 세로 크기
    # M : 가로 크기
    # 1 <= N, M <= 20
    n, m = map(int, input().split())
    board = [input() for _ in range(n)]

    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

    print(solution())
