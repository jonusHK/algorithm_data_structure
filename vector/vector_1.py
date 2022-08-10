"""
백준 - 늑대와 양
"""

r, c = map(int, input().split())
m = []
for _ in range(r):
    _m = []
    for w in input():
        if w == '.':
            _m.append('D')
        else:
            _m.append(w)
    m.append(_m)

dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]


def defend(x, y, li):
    global ck
    for _i in range(4):
        _x, _y = x + dx[_i], y + dy[_i]
        if _x == len(li) or _x < 0 or _y == len(li[0]) or _y < 0:
            continue
        if li[_x][_y] == 'D':
            continue
        if li[_x][_y] == 'S':
            ck = True


ck = False
for i in range(r):
    for j in range(c):
        if m[i][j] == 'W':
            defend(i, j, m)
            if ck:
                break
    if ck:
        break

if ck:
    print(0)
else:
    print(1)
    for _m in m:
        print(''.join(_m))
