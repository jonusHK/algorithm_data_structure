"""
백준 - 트리의 높이와 너비
"""
import sys


class Node:
    def __init__(self, num: int, left: int, right: int):
        self.num = num
        self._parent = -1
        self._left = left
        self._right = right

    @property
    def parent(self):
        return self._parent

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    @parent.setter
    def parent(self, value):
        self._parent = value

    @left.setter
    def left(self, value):
        self._left = value

    @right.setter
    def right(self, value):
        self._right = value


def dfs(num: int, level: int):
    global depth, width
    depth = max(depth, level)
    if tree[num].left != -1:
        dfs(tree[num].left, level + 1)
    level_min[level] = min(level_min[level], width)
    level_max[level] = max(level_max[level], width)
    width += 1
    if tree[num].right != -1:
        dfs(tree[num].right, level + 1)


_input = sys.stdin.readline

n = int(_input())
tree = {}
root = -1
depth = 1
width = 1
level_min = [n]
level_max = [0]

# 초기화
for i in range(1, n + 1):
    tree[i] = Node(i, -1, -1)
    level_min.append(n)
    level_max.append(0)

for _ in range(n):
    node, left_node, right_node = map(int, _input().split())
    tree[node].left = left_node
    tree[node].right = right_node
    if left_node != -1:
        tree[left_node].parent = node
    if right_node != -1:
        tree[right_node].parent = node

for i in range(1, n + 1):
    if tree[i].parent == -1:
        root = i
        break

dfs(root, 1)

result_level = 1
max_width = 1
for i in range(2, depth + 1):
    w = level_max[i] - level_min[i] + 1
    if w > max_width:
        result_level = i
        max_width = w

print(result_level, max_width)
