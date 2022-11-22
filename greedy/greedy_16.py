"""
백준 - 근우의 다이어리 꾸미기
"""

n = str(input())

if n == '0':
    print(1)
else:
    rng = 10
    array = [0] * 10

    int_n = int(n)
    cnt = len(n)
    for i in range(1, len(array)):
        if array[int(i)] > 0:
            continue

        copy_cnt = cnt
        while copy_cnt >= 1:
            multi_v = int(str(i) * copy_cnt)
            if int_n >= multi_v:
                array[i] = copy_cnt
                break
            copy_cnt -= 1

    print(max(array))


# 다른 풀이) 규칙 & 최적화
# n = input()
# s = '1' * len(n)
#
# if int(n) >= int(s):
#     print(len(n))
# else:
#     print(len(n) - 1)
