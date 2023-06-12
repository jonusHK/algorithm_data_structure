"""
백준 - 트리
"""


def dfs(node):

    if not tree[node]:
        return 1

    cnt = 0
    for child_node in tree[node]:
        cnt += dfs(child_node)

    return cnt


def solution(remove_node):
    leaf_node_cnt = sum([1 for t in tree if not t])

    answer = leaf_node_cnt - dfs(remove_node)

    for i in range(len(tree)):
        if remove_node in tree[i] and len(tree[i]) == 1:
            answer += 1

    return answer


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    tree = [[] for _ in range(n)]
    for i in range(len(arr)):
        if arr[i] != -1:
            tree[arr[i]].append(i)

    print(solution(int(input())))
