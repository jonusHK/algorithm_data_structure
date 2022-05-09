from collections import defaultdict, deque

n = int(input())
m = int(input())

adj = defaultdict(list)
visited = [False] * n
for _ in range(m):
    n1, n2 = map(int, input().split())
    adj[n1].append(n2)
    adj[n2].append(n1)

q = deque([1])
array = [False] * (n + 1)

while q:
    pop_val = q.popleft()
    if not array[pop_val]:
        for v in adj[pop_val]:
            if not array[v]:
                q.append(v)
        array[pop_val] = True

print(len([v for v in array if v]) - 1)
