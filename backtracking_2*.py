"""
백준 - 알파벳
"""

# 이동 좌표 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global result
    q = set()
    q.add((x, y, array[x][y]))

    while q:
        x, y, step = q.pop()
        result = max(result, len(step))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and array[nx][ny] not in step:
                q.add((nx, ny, step + array[nx][ny]))


r, c = map(int, input().split())
array = []
for _ in range(r):
    array.append(input())

result = 0
bfs(0, 0)
print(result)

# 아래와 같이 DFS 로 구현 가능하나, 시간 초과됨
# all_pos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#
#
# def get_paths(_pos: tuple, _checked: list):
#     _paths = []
#     for _p in all_pos:
#         try:
#             _dy = _pos[0] + _p[0]
#             _dx = _pos[1] + _p[1]
#             if _dy >= 0 and _dx >= 0 and array[_dy][_dx] not in _checked:
#                 _paths.append((_dy, _dx))
#         except IndexError:
#             continue
#
#     return _paths
#
#
# def dfs(_pos: tuple, _checked: list, _cnt: int):
#     global cnt
#     paths = get_paths(_pos, _checked)
#     if not paths:
#         cnt = max(cnt, _cnt)
#         return
#
#     for next_pos in paths:
#         _checked.append(array[next_pos[0]][next_pos[1]])
#         _cnt += 1
#         dfs(next_pos, _checked, _cnt)
#         _checked.pop()
#         _cnt -= 1
#
#
# r, c = map(int, input().split())
#
# array = []
# for _ in range(r):
#     array.append(input())
#
# cnt = 1
# dfs((0, 0), [array[0][0]], cnt)
#
# print(cnt)
