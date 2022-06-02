"""
백준 - N-Queen
"""


def check(cur_row):
    for _r in range(cur_row):
        # 위아래에 존재하는 경우
        if row[cur_row] == row[_r]:
            return False
        # 대각선에 존재하는 경우
        if abs(row[cur_row] - row[_r]) == cur_row - _r:
            return False
    return True


def dfs(cur_row):
    global result
    if cur_row == n:
        result += 1
    else:
        for cur_col in range(n):
            row[cur_row] = cur_col
            if check(cur_row):
                dfs(cur_row + 1)


n = int(input())
row = [0] * n
result = 0
dfs(0)
print(result)
