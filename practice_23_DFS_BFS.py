import sys


def checked(stack, li):
    if not li[1] and li[0] not in stack:
        return False
    return True


def find_parent(dict, child_node):
    for k, v in dict.items():
        for tu in v:
            if tu[0] == child_node:
                return k
    return -1


def calc_dfs(dict, first_node):
    dfs_stack = []
    next_node = first_node
    dfs_stack.append(next_node)
    while True:
        if dict.get(next_node, False):
            child_exist = False
            for next_li in dict[next_node]:
                if not checked(dfs_stack, next_li):
                    next_node = next_li[0]
                    dfs_stack.append(next_node)
                    next_li[1], child_exist = True, True
                    break
            if not child_exist:
                parent_node = find_parent(dict, next_node)
                if parent_node == -1:
                    break
                else:
                    next_node = parent_node
        else:
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
    try:
        dict = {}
        first_node = first_info[2]
        for con in connected:
            value = dict.get(con[0], [])
            value.append([con[1], False])
            dict.update({ con[0]: sorted(value, key=lambda v: v[0]) })

        dfs_stack = calc_dfs(dict, first_node)
        bfs_queue = calc_bfs(dict, first_node)
        print('dfs --- ', ' '.join([str(dfs) for dfs in dfs_stack]))
        print('bfs --- ', ' '.join([str(bfs) for bfs in bfs_queue]))
        
    except Exception as e:
        raise e


if __name__ == '__main__':
    first_info  = list(map(int, sys.stdin.readline().split()))
    connected = []
    i = 0
    while first_info[1] > i:
        connected.append(tuple(map(int, sys.stdin.readline().split())))
        i += 1

    # first_info = [8, 8, 1]
    # connected = [(1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (3, 7), (5, 8), (8, 6)]
    solution(first_info, connected)
    
