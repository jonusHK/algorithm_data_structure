"""
프로그래머스 - 게임 맵 최단거리
"""


from collections import deque

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]


def solution(maps):
    n, m = len(maps), len(maps[0])
    new_maps = [
        [
            maps[i-1][j-1] if 0 < i <= n and 0 < j <= m else 0
            for j in range(m + 1)
        ] for i in range(n + 1)
    ]

    x, y = 1, 1
    visited = [[0] * (m + 1) for _ in range(n + 1)]
    visited[x][y] = 1
    q = deque([(x, y, visited, 1)])

    while q:
        x, y, visited, count = q.popleft()

        if x == n and y == m:
            return count

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 < nx <= n and 0 < ny <= m and new_maps[nx][ny] == 1:
                if visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny, visited, count + 1))

    return -1


if __name__ == "__main__":
    maps = [[1,0,1,1,1], [1,0,1,0,1], [1,0,1,1,1], [1,1,1,0,1], [0,0,0,0,1]]
    print(solution(maps))
