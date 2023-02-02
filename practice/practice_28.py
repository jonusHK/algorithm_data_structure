from typing import List

r, c = map(int, input().split())
board: List[str] = [input() for _ in range(r)]

max_cnt = 0


def bfs(x: int, y: int):
    global max_cnt

    q = {(x, y, board[x][y])}
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    while q:
        px, py, sequence = q.pop()
        max_cnt = max(max_cnt, len(sequence))
        for idx in range(4):
            _x = px + dx[idx]
            _y = py + dy[idx]
            if 0 <= _x < r and 0 <= _y < c and board[_x][_y] not in sequence:
                q.add((_x, _y, sequence + board[_x][_y]))


bfs(0, 0)

print(max_cnt)
