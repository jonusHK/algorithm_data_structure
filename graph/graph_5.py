"""
백준 - DFS와 BFS
"""


from collections import defaultdict, deque


def dfs(graph, v, visited):
    arr = []
    stack = [v]

    while stack:
        node = stack.pop()

        if visited[node]:
            continue

        visited[node] = 1
        arr.append(str(node))

        for n in sorted(graph[node], reverse=True):
            if not visited[n]:
                stack.append(n)

    return ' '.join(arr)


def bfs(graph, v, visited):
    arr = []
    q = deque([v])

    while q:
        node = q.popleft()

        if visited[node]:
            continue

        visited[node] = 1
        arr.append(str(node))

        for n in sorted(graph[node]):
            if not visited[n]:
                q.append(n)

    return ' '.join(arr)


if __name__ == "__main__":
    n, m, v = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    print(dfs(graph, v, [0] * 1001))
    print(bfs(graph, v, [0] * 1001))
