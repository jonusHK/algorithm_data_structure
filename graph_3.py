import sys
sys.setrecursionlimit(10 ** 4)  # 기본적으로 재귀 횟수를 1000 정도로 설정해놓음


def dst(cur_pos: tuple):
    visited[cur_pos[1]][cur_pos[0]] = True
    for _i in range(4):
        next_pos_x = cur_pos[0] + dx[_i]
        next_pos_y = cur_pos[1] + dy[_i]
        if 0 <= next_pos_x < m and 0 <= next_pos_y < n and position[next_pos_y][next_pos_x]:
            if not visited[next_pos_y][next_pos_x]:
                dst((next_pos_x, next_pos_y))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

rst = []
t = int(input())
for idx in range(t):
    m, n, k = map(int, input().split())
    cnt = 0

    position = [[False for _ in range(m)] for _ in range(n)]
    visited = [[False for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        position[y][x] = True

    for i in range(n):
        for j in range(m):
            if position[i][j] and not visited[i][j]:
                dst((j, i))
                cnt += 1

    rst.append(cnt)

for cnt in rst:
    print(cnt)
