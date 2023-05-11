"""
백준 - 벽 부수고 이동하기
"""


from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def next_pos(arr, x, y, broken):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 1 <= nx <= n and 1 <= ny <= m:
            # 벽이 없는 경우
            if not arr[nx][ny]:
                yield nx, ny, broken

            # 벽이 있고, 이전에 벽을 부순 적이 없는 경우
            elif not broken:
                yield nx, ny, 1


def bfs(arr, n, m):
    q = deque([(1, 1, 1, 0)])
    visited = [[[0] * 2 for _ in range(m + 1)] for _ in range(n + 1)]
    visited[1][1][0] = 1

    while q:
        x, y, d, b = q.popleft()

        if x == n and y == m:
            return d

        for nx, ny, nb in next_pos(arr, x, y, b):
            if not visited[nx][ny][nb]:
                visited[nx][ny][nb] += 1
                q.append((nx, ny, d + 1, nb))

    return -1


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        row = input()
        for j in range(m):
            arr[i][j+1] = int(row[j])

    print(bfs(arr, n, m))
