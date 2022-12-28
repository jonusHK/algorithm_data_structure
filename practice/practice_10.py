from collections import deque
from typing import List, Tuple

n, m = map(int, input().split())
array: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]

sm = 100000000
bg = 1
for _ in range(m):
    x, y, weight = map(int, input().split())
    array[x].append((y, weight))
    array[y].append((x, weight))
    sm = min(sm, weight)
    bg = max(bg, weight)

start, end = map(int, input().split())


def find_max(st: int, ed: int):
    global sm, bg

    result = sm
    while sm <= bg:
        visited: List[bool] = [i == st for i in range(n + 1)]
        mid = (bg + sm) // 2
        q = deque([st])
        while q:
            num = q.popleft()
            for tu in array[num]:
                if tu[1] >= mid and not visited[tu[0]]:
                    visited[tu[0]] = True
                    q.append(tu[0])
                    if tu[0] == ed:
                        break
            if visited[ed]:
                break
        if visited[ed]:
            result = mid
            sm = mid + 1
        else:
            bg = mid - 1

    return result


print(find_max(start, end))
