"""
백준 - 이분 그래프
"""


import sys

sys.setrecursionlimit(10**6)
_input = sys.stdin.readline


def dfs(node, flag):

    visited[node] = flag

    for i in graph[node]:
        if visited[i]:
            if visited[i] == flag:
                return False
        else:
            if not dfs(i, flag * -1):
                return False

    return True


def solution():
    for i in range(V + 1):
        if visited[i]:
            continue

        if not dfs(i, 1):
            return "NO"

    return "YES"


if __name__ == "__main__":

    answer = []
    for _ in range(int(_input())):
        V, E = map(int, _input().split())
        graph = [[] for _ in range(V + 1)]
        visited = [0] * (V + 1)

        for _ in range(E):
            u, v = map(int, _input().split())
            graph[u].append(v)
            graph[v].append(u)

        answer.append(solution())

    for a in answer:
        print(a)
