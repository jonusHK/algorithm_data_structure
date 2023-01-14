import sys

n = int(input())
crane_weights = list(map(int, input().split()))
m = int(input())
box_weights = list(map(int, input().split()))

box_weights.sort(reverse=True)
crane_weights.sort(reverse=True)


if box_weights[0] > crane_weights[0]:
    print(-1)
    sys.exit()


positions = [0] * n
checked = [False] * m
time = 0
cnt = 0
while cnt != m:
    for i in range(n):
        while positions[i] < m:
            if not checked[positions[i]] and crane_weights[i] >= box_weights[positions[i]]:
                checked[positions[i]] = True
                positions[i] += 1
                cnt += 1
                break
            positions[i] += 1
    time += 1
print(time)
