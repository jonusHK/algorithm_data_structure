n, k = map(int, input().split())
products = [tuple(map(int, input().split())) for _ in range(n)]

max_num = 0


def backtracking(idx: int, cur_value: int, left_weight: int):
    global max_num
    max_num = max(max_num, cur_value)

    for j in range(idx + 1, n):
        if left_weight >= products[j][0]:
            backtracking(j, cur_value + products[j][1], left_weight - products[j][0])


for i in range(n):
    if k >= products[i][0]:
        backtracking(i, products[i][1], k - products[i][0])


print(max_num)
