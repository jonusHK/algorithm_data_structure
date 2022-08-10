n = int(input())


num, cnt = 1, 0

while n > 0:
    if num > n:
        num = 1
    n -= num
    num += 1
    cnt += 1

print(cnt)
