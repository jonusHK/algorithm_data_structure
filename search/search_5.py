n, m = map(int, input().split(' '))

li = []
for _ in range(n):
    li.append(input())


empty_rows = []
for c in range(n):
    if 'X' not in li[c]:
        empty_rows.append(c)

cnt = 0
for c in range(m):
    exist = False
    for r in range(n):
        if li[r][c] == 'X':
            exist = True
    if not exist:
        if empty_rows:
            empty_rows.pop(0)
        cnt += 1

if empty_rows:
    cnt += len(empty_rows)

print(cnt)
