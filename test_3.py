def solution(U, L, C):
    rst_li = [['0' for _ in range(len(C))] for _ in range(2)]
    check_li = [False for _ in range(len(C))]
    for idx, val in enumerate(C):
        if val == 2:
            rst_li[0][idx], rst_li[1][idx] = '1', '1'
            check_li[idx] = True
            U -= 1
            L -= 1
        elif val == 0:
            check_li[idx] = True

    for idx, val in enumerate(check_li):
        if val == False:
            if U > 0:
                rst_li[0][idx] = '1'
                U -= 1
            else:
                rst_li[1][idx] = '1'
                L -= 1

    if U > 0 or L > 0:
        return "IMPOSSIBLE"

    rst = ''
    for i in range(len(rst_li)):
        rst += ''.join(rst_li[i])
        if (i != len(rst_li) - 1):
            rst += ','

    return rst

print(solution(2, 3, [0, 0, 1, 1, 2]))
