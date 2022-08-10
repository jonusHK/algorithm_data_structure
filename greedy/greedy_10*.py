"""
백준 - 배
"""

import sys

n = int(input())
cranes = list(map(int, input().split()))
m = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
    sys.exit()

times = 0
cnt = 0
positions = [0] * n
checked = [False] * m

while True:
    if cnt == m:
        break
    for i in range(n):
        while positions[i] < m:
            if not checked[positions[i]] and cranes[i] >= boxes[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                cnt += 1
                break
            positions[i] += 1

    times += 1

print(times)
