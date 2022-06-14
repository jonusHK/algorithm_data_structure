"""
백준 - 이름궁합 테스트
"""

n, m = map(int, input().split())
a, b = input().split()

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

min_len = min(n, m)

s = ''
for i in range(min_len):
    s += a[i] + b[i]

s += a[min_len:] + b[min_len:]

array = [alp[ord(i) - ord('A')] for i in s]

for i in range(n+m-2):
    for j in range(n+m-1-i):
        array[j] += array[j+1]
        array[j] %= 10

print('{}%'.format(array[0] * 10 + array[1] * 1))
