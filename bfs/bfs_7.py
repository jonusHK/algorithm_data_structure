"""
백준 - Mooyo Mooyo
"""


from collections import deque

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
n, k = map(int, input().split())
w = 10
first_step = True

mapping = [list(map(int, input())) for _ in range(n)]


def get_ck():
    return [[False] * w for _ in range(n)]


def fill_to_bottom():
    for _j in range(w):
        rows = [mapping[_i][_j] for _i in range(n)]
        nums = [_num for _num in rows if _num != 0]
        diff = len(rows) - len(nums)
        while diff != 0:
            nums = [0] + nums
            diff -= 1

        for _idx, _num in enumerate(nums):
            mapping[_idx][_j] = _num


def set_zero():
    for _i in range(n):
        for _j in range(w):
            if temp_visited[_i][_j] is True:
                mapping[_i][_j] = 0


def bfs(_i: int, _j: int):
    _cnt = 1
    q = deque([(_i, _j)])
    visited[_i][_j], temp_visited[_i][_j] = True, True

    while q:
        cur_x, cur_y = q.popleft()
        for _idx in range(4):
            x = cur_x + dx[_idx]
            y = cur_y + dy[_idx]
            if x < 0 or x >= n or y < 0 or y >= w:
                continue
            if mapping[cur_x][cur_y] == mapping[x][y] and visited[x][y] is False:
                q.append((x, y))
                visited[x][y], temp_visited[x][y] = True, True
                _cnt += 1

    return _cnt


while True:
    exists = False
    visited = get_ck()
    for i in range(n):
        for j in range(w):
            temp_visited = get_ck()
            if mapping[i][j] != 0 and visited[i][j] is False:
                cnt = bfs(i, j)
                if cnt >= k:
                    set_zero()
                    exists = True

    if not exists:
        break

    fill_to_bottom()


for row in mapping:
    for idx, num in enumerate(row):
        print(num) if idx == w - 1 else print(num, end='')
