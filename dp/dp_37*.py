"""
백준 - ACM craft
"""


from collections import deque


def solution(n, w):

    q = deque([])
    for i in range(1, n + 1):
        if not level[i]:
            q.append(i)
            level[i] -= 1

    while q:
        b = q.popleft()

        if b == w:
            break

        for nb in mapper[b]:
            dp[nb] = max(dp[nb], dp[b] + d[nb])
            level[nb] -= 1

        for i in range(1, n + 1):
            if not level[i]:
                q.append(i)
                level[i] -= 1

    return dp[w]


if __name__ == "__main__":
    t = int(input())

    answer = []
    for _ in range(t):
        n, k = map(int, input().split())
        d = [0] + list(map(int, input().split()))

        mapper = [[] for _ in range(n + 1)]
        level = [0] * (n + 1)
        for _ in range(k):
            x, y = map(int, input().split())
            mapper[x].append(y)
            level[y] += 1

        w = int(input())

        dp = [d[i] for i in range(n + 1)]

        answer.append(solution(n, w))

    for a in answer:
        print(a)
