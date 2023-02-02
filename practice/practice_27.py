from copy import deepcopy
from typing import List, Set

r, c = map(int, input().split())
board: List[str] = [input() for _ in range(r)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

max_cnt = 0


def dfs(x: int, y: int, _visited: Set[str], _cnt: int):
    global max_cnt

    _cnt += 1
    _visited.add(board[x][y])
    max_cnt = max(_cnt, max_cnt)

    for idx in range(4):
        _x = x + dx[idx]
        _y = y + dy[idx]
        if 0 <= _x < r and 0 <= _y < c and board[_x][_y] not in _visited:
            dfs(_x, _y, deepcopy(_visited), _cnt)

    _visited.remove(board[x][y])


visited = set()

dfs(0, 0, visited, 0)

print(max_cnt)
