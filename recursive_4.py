"""
백준 - Z
"""


def recursive(sz, x, y):
    if sz == 1:
        return 0
    sz //= 2
    for i in range(2):
        for j in range(2):
            if x < sz * (i + 1) and y < sz * (j + 1):
                return (i * 2 + j) * sz * sz + recursive(sz, x-sz*i, y-sz*j)


n, r, c = map(int, input().split())

print(recursive(2 ** n, r, c))


# 방법2) 모든 리스트에 숫자 넣어야 할 때 사용
# def recursive(s_1: int, e_1: int, s_2: int, e_2: int):
#     global last_num
#
#     if e_1 - s_1 == 2:
#         for i in range(s_1, e_1):
#             for j in range(s_2, e_2):
#                 if i == 0 and j == 0:
#                     continue
#                 last_num += 1
#                 array[i][j] = last_num
#         return
#
#     new_1 = s_1 + (e_1 - s_1) // 2
#     new_2 = s_2 + (e_2 - s_2) // 2
#
#     recursive(s_1, new_1, s_2, new_2)
#     recursive(s_1, new_1, new_2, e_2)
#     recursive(new_1, e_1, s_2, new_2)
#     recursive(new_1, e_1, new_2, e_2)
#
#
# n, r, c = map(int, input().split())
#
# len_array = 2 ** n
# array = [[0 for _ in range(len_array)] for _ in range(len_array)]
# last_num = 0
# recursive(0, len_array, 0, len_array)
#
# print(array[r][c])
