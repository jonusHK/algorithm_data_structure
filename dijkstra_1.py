import heapq


def dijkstra(start):
    q = []
    times[start] = 0
    heapq.heappush(q, (times[start], start))

    while q:
        current_time, current_num = heapq.heappop(q)

        if times[current_num] < current_time:
            continue

        for _next_time, _next_num in mapping[current_num]:
            _time = current_time + _next_time

            if _time < times[_next_num]:
                times[_next_num] = _time
                heapq.heappush(q, [_time, _next_num])


inf_num = float('inf')
t = int(input())
for _ in range(t):
    n, d, c = map(int, input().split())

    mapping = [[] for _ in range(n + 1)]
    times = [inf_num] * (n + 1)
    for _ in range(d):
        a, b, s = map(int, input().split())
        mapping[b].append((s, a))

    dijkstra(c)
    cnt, max_time = 0, -1

    for _time in times[1:]:
        if _time < inf_num:
            cnt += 1
            max_time = max(_time, max_time)

    print(cnt, max_time)
