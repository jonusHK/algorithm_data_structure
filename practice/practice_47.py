import sys

sys.setrecursionlimit(10**6)

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]

dp = [[0] * 100 for _ in range(100)]
visited = [[0] * 100 for _ in range(100)]
heights = []


def dfs(x, y, h, m, n):

    if dp[x][y] > h:
        return dp[x][y], 1

    if x == m - 1 and y == n - 1:
        dp[x][y] = heights[x][y]
        return dp[x][y], 1

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue

        if heights[nx][ny] <= h:
            continue

        if visited[nx][ny]:
            continue

        rst = dfs(nx, ny, h, m, n)
        if rst[1]:
            dp[x][y] = min(heights[x][y], rst[0])
            visited[x][y] = 0
            return dp[x][y], 1

    visited[x][y] = 0

    return dp[x][y], 0


def solution(h):
    global heights

    heights = h

    m = len(heights)
    n = len(heights[0])

    answer = min(heights[0][0], heights[m-1][n-1])
    s = 0
    e = answer - 1

    while s <= e:
        mid = (s + e) // 2
        rst = dfs(0, 0, mid, m, n)

        if rst[1] and rst[0] > mid:
            s = mid + 1
        else:
            answer = mid
            e = mid - 1

    return answer


if __name__ == "__main__":
    heights = [
        [5, 5, 5, 6, 1, 2],
        [3, 3, 5, 4, 5, 5],
        [3, 2, 5, 2, 5, 6]
    ]
    print(solution(heights))
