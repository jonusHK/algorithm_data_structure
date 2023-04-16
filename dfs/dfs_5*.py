"""
프로그래머스 - 미로 탈출 명령어
"""

dx = (-1, 0, 0, 1)
dy = (0, 1, -1, 0)
d = ('u', 'r', 'l', 'd')


def get_routes(n, m, x, y):
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]

        if 0 < next_x <= n and 0 < next_y <= m:
            yield next_x, next_y, d[i]


def dfs(n, m, x, y, r, c, k):
    stack = [(x, y, '')]

    while stack:
        cur_x, cur_y, cur_route = stack.pop()

        if len(cur_route) == k and (cur_x, cur_y) == (r, c):
            return cur_route

        shortest_cnt = abs(r - cur_x) + abs(c - cur_y)
        remain_cnt = k - len(cur_route)

        if remain_cnt < shortest_cnt or (remain_cnt - shortest_cnt) % 2 == 1:
            continue

        for next_x, next_y, next_d in get_routes(n, m, cur_x, cur_y):
            stack.append((next_x, next_y, cur_route + next_d))


def solution(n, m, x, y, r, c, k):
    result = dfs(n, m, x, y, r, c, k)

    if not result:
        return 'impossible'

    return result


if __name__ == "__main__":
    print(solution(3, 4, 2, 3, 3, 1, 5))
    # print(solution(2, 2, 1, 1, 2, 2, 2))
    # print(solution(3, 3, 1, 2, 3, 3, 4))
