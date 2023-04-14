"""
프로그래머스 - 표 병합
"""


def update(arr, parent, *args):
    assert len(args) in (2, 3)

    if len(args) == 2:
        # UPDATE value1 value2
        for i in range(1, len(arr)):
            for j in range(1, len(arr[i])):
                if arr[i][j] == args[0]:
                    arr[i][j] = args[1]
    else:
        # UPDATE r c value
        r, c = find(parent, int(args[0]), int(args[1]))
        arr[r][c] = args[2]


def find(parent, row, column):
    while True:
        coord = parent[row][column]
        if not coord:
            break
        row, column = coord[0], coord[1]

    return row, column


def union(arr, parent, r1, c1, r2, c2):
    parent[r2][c2] = (r1, c1)
    arr[r2][c2] = None


def merge(arr, parent, *args):
    # MERGE r1 c1 r2 c2
    assert len(args) == 4

    r1, c1 = find(parent, int(args[0]), int(args[1]))
    r2, c2 = find(parent, int(args[2]), int(args[3]))

    if (r1, c1) == (r2, c2):
        return

    if arr[r1][c1]:
        union(arr, parent, r1, c1, r2, c2)
    else:
        union(arr, parent, r2, c2, r1, c1)


def unmerge(arr, parent, *args):
    # UNMERGE r c
    assert len(args) == 2

    r, c = int(args[0]), int(args[1])
    parent_r, parent_c = find(parent, r, c)

    unmerge_arr = []
    for i in range(1, len(parent)):
        for j in range(1, len(parent[i])):
            if find(parent, i, j) == (parent_r, parent_c):
                unmerge_arr.append((i, j))

    for i, j in unmerge_arr:
        parent[i][j] = None

    if (r, c) == (parent_r, parent_c):
        return

    arr[r][c] = arr[parent_r][parent_c]
    arr[parent_r][parent_c] = None


def print_(arr, parent, *args):
    # PRINT r c
    assert len(args) == 2

    r, c = find(parent, int(args[0]), int(args[1]))
    return arr[r][c] or 'EMPTY'


def handle(arr, parent, *args):
    if args[0] == 'UPDATE':
        update(arr, parent, *args[1:])
    elif args[0] == 'MERGE':
        merge(arr, parent, *args[1:])
    elif args[0] == 'UNMERGE':
        unmerge(arr, parent, *args[1:])
    else:
        return print_(arr, parent, *args[1:])


def init():
    arr, parent = [], []
    for _ in range(51):
        arr.append([None] * 51)
        parent.append([None] * 51)

    return arr, parent


def solution(commands):
    arr, parent = init()
    result = []
    for command in commands:
        value = handle(arr, parent, *command.split())
        if value:
            result.append(value)

    return result


if __name__ == "__main__":
    commands = [
        "UPDATE 1 1 menu", "UPDATE 1 2 category", "UPDATE 2 1 bibimbap", "UPDATE 2 2 korean",
        "UPDATE 2 3 rice", "UPDATE 3 1 ramyeon", "UPDATE 3 2 korean", "UPDATE 3 3 noodle",
        "UPDATE 3 4 instant", "UPDATE 4 1 pasta", "UPDATE 4 2 italian", "UPDATE 4 3 noodle",
        "MERGE 1 2 1 3", "MERGE 1 3 1 4", "UPDATE korean hansik", "UPDATE 1 3 group", "UNMERGE 1 4",
        "PRINT 1 3", "PRINT 1 4"
    ]
    print(solution(commands))
