import sys


def find_parent(dict, child_node):
    for k, v in dict.items():
        for li in v:
            if li[0] == child_node:
                if not li[1]:
                    return k
                return k
    return -1


def not_checked_all(dict):
    for k, v in dict.items():
        for li in v:
            if not li[1]:
                return True
    return False


def calc_dfs(dict, first_node):
    next_node = first_node
    dfs_stack = [next_node]
    while not_checked_all(dict):
        child_exist = False
        for next_li in dict[next_node]:
            if not next_li[1]:
                next_li[1] = True
                if next_li[0] not in dfs_stack:
                    next_node = next_li[0]
                    dfs_stack.append(next_node)
                    child_exist = True
                    break
        if not child_exist:
            parent_node = find_parent(dict, next_node)
            if parent_node == -1: 
                break
            else:
                next_node = parent_node
    return dfs_stack


def calc_bfs(dict, first_node):
    bfs_queue = []
    bfs_queue.append(first_node)
    pointer = 0
    while len(bfs_queue) > pointer:
        next_node = bfs_queue[pointer]
        if dict.get(next_node, False):
            for child_node in dict[next_node]:
                if child_node[0] not in bfs_queue:
                    bfs_queue.append(child_node[0])
        pointer += 1
    return bfs_queue


def solution(first_info, connected):
    dict = {}
    first_node = first_info[2]
    for con in connected:
        for idx, val in enumerate(con):
            value = dict.get(val, [])
            value.append([con[len(con) - idx - 1], False])
            dict.update({ val: sorted(value, key=lambda v: v[0]) })

    dfs_stack = calc_dfs(dict, first_node)
    bfs_queue = calc_bfs(dict, first_node)
    print(' '.join([str(dfs) for dfs in dfs_stack]))
    print(' '.join([str(bfs) for bfs in bfs_queue]))

if __name__ == '__main__':
    first_info  = list(map(int, sys.stdin.readline().split()))
    connected = []
    i = 0
    while first_info[1] > i:
        connected.append(tuple(sorted(map(int, sys.stdin.readline().split()))))
        i += 1

    solution(first_info, connected)