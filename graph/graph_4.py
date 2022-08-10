"""
백준 - 효율적인 해킹
"""
from collections import deque


def bfs(node: int):
    cnt = 1
    q = deque([node])
    visited = [False for _ in range(n + 1)]
    visited[node] = True

    while q:
        v = q.popleft()
        for _v in adj[v]:
            if not visited[_v]:
                visited[_v] = True
                q.append(_v)
                cnt += 1

    return cnt


n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[b].append(a)

max_cnt = 0
rst = []
for i in range(1, n + 1):
    cnt = bfs(i)
    if cnt >= max_cnt:
        if cnt == max_cnt:
            rst.append(i)
        else:
            rst = [i]

        max_cnt = cnt

for v in rst:
    print(v, end=' ')
