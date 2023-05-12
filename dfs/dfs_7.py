"""
백준 - 유기농 배추
"""


import sys
from copy import deepcopy

sys.setrecursionlimit(10**6)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def next_pos(arr, x, y, m, n):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny]:
            yield nx, ny


def dfs(arr, visited, x, y, m, n):
    visited[x][y] = 1

    for nx, ny in next_pos(arr, x, y, m, n):
        if visited[nx][ny]:
            continue

        dfs(arr, visited, nx, ny, m, n)


def solution(arr, target, visited, m, n):
    cnt = 0
    for x, y in target:
        if visited[x][y]:
            continue

        dfs(arr, visited, x, y, m, n)
        cnt += 1

    return cnt


if __name__ == "__main__":

    t = int(input())

    rst = []
    for _ in range(t):
        m, n, k = map(int, input().split())

        arr = [[0] * m for _ in range(n)]
        visited = deepcopy(arr)
        target = []

        for _ in range(k):
            x, y = map(int, input().split())

            arr[y][x] = 1
            target.append((y, x))

        rst.append(solution(arr, target, visited, m, n))

    for r in rst:
        print(r)
