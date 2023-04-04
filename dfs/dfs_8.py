"""
프로그래머스 - 아이템 줍기
"""


from copy import deepcopy

min_cnt = 1e9
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def find_path(rectangle, cur_x, cur_y):
    for i in range(4):
        x = cur_x + dx[i]
        y = cur_y + dy[i]
        half_x = cur_x + dx[i] / 2
        half_y = cur_y + dy[i] / 2

        is_inner = False
        is_line = False
        for r in rectangle:
            if (
                (half_x > r[0] and half_y > r[1]) and
                (half_x < r[2] and half_y < r[3])
            ):
                is_inner = True
                break

            check = 0
            for _x, _y in zip((x, cur_x), (y, cur_y)):
                if (
                    (_x in [r[0], r[2]] and r[1] <= _y <= r[3]) or
                    (_y in [r[1], r[3]] and r[0] <= _x <= r[2])
                ):
                    check += 1

            if check == 2:
                is_line = True

        if not is_inner and is_line:
            yield x, y


def dfs(rectangle, cur_x, cur_y, final_x, final_y, visited, cnt):
    global min_cnt

    visited[cur_x][cur_y] = 1

    if cur_x == final_x and cur_y == final_y:
        min_cnt = min(min_cnt, cnt)
        return

    for x, y in find_path(rectangle, cur_x, cur_y):
        if visited[x][y] == 0:
            dfs(rectangle, x, y, final_x, final_y, deepcopy(visited), cnt + 1)


def solution(rectangle, characterX, characterY, itemX, itemY):
    visitied = [[0] * 51 for _ in range(51)]
    dfs(rectangle, characterX, characterY, itemX, itemY, visitied, 0)
    return min_cnt


if __name__ == '__main__':
    rectangle = [
        [1, 1, 7, 4],
        [3, 2, 5, 5],
        [4, 3, 6, 9],
        [2, 6, 8, 8]
    ]
    character_x = 1
    character_y = 3
    item_x = 7
    item_y = 8
    print(solution(rectangle, character_x, character_y, item_x, item_y))
