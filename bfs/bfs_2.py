from collections import deque


MAX = 100001
n, k = map(int, input().split())
array = [0] * MAX


def bfs():
    q = deque([n])
    while q:
        pos = q.popleft()

        if pos == k:
            return array[pos]

        for next_pos in (pos - 1, pos + 1, pos * 2):
            if 0 <= next_pos < MAX and not array[next_pos]:
                array[next_pos] = array[pos] + 1
                q.append(next_pos)

print(bfs())
