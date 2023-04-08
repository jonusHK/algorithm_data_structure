from copy import deepcopy

coins_arr = []
m = 0
n = 0
max_cnt = 0
dx = [1, 1, 1]
dy = [-1, 0, 1]


def route(coord, visited):
    for i in range(3):
        x = coord[0] + dx[i]
        y = coord[1] + dy[i]

        if (
            0 <= x < m and 0 <= y < n
            and visited[x][y] != 1
        ):
            yield x, y


def dfs(first, second, visited, cnt):
    global max_cnt

    cnt += coins_arr[first[0]][first[1]] + coins_arr[second[0]][second[1]]
    if first[0] == m - 1 or first[1] == m - 1:
        max_cnt = max(max_cnt, cnt)
        return

    copy_visited = deepcopy(visited)
    for x, y in route(first, copy_visited):
        copy_visited[x][y] = 1
        for _x, _y in route(second, copy_visited):
            copy_visited[_x][_y] = 1
            dfs((x, y), (_x, _y), copy_visited, cnt)
            copy_visited[_x][_y] = 0
        copy_visited[x][y] = 0


def solution(coins):
    global coins_arr, m, n

    coins_arr = coins
    m = len(coins_arr)
    n = len(coins[0])
    first = (0, 0)
    second = (0, n - 1)
    visited = [[0] * n for _ in range(m)]
    visited[first[0]][first[1]] = visited[second[0]][second[1]] = 1
    dfs(first, second, visited, 0)
    return max_cnt


if __name__ == "__main__":
    coins = [[4, 0, 1], [3, 6, 2], [5, 7, 7], [4, 2, 2]]
    print(solution(coins))
