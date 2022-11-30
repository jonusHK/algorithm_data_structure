"""
dijkstra 알고리즘
"""

import heapq

inf_num = float('inf')

mapping = {
    'a': [('b', 8), ('c', 1), ('d', 2)],
    'b': [],
    'c': [('b', 5), ('d', 2)],
    'd': [('e', 3), ('f', 5)],
    'e': [('f', 1)],
    'f': [('a', 5)]
}

start_node, end_node = 'a', 'f'
distance, tracker = {}, {}
for n in mapping.keys():
    distance[n] = inf_num if n != start_node else 0
    tracker[n] = None if n != start_node else start_node


def dijkstra(start_n: str):
    distance[start_n] = 0
    q = [(start_n, 0)]
    heapq.heapify(q)

    while q:
        pop_n, pop_v = heapq.heappop(q)
        for n, v in mapping[pop_n[0]]:
            new_v = pop_v + v
            if distance[n] > new_v:
                distance[n] = new_v
                tracker[n] = pop_n
                heapq.heappush(q, (n, new_v))


dijkstra(start_node)

# 최소 거리
print('최소 거리 :', distance[end_node])

# 최소 경로
node = end_node
path = [node]
while tracker[node] != node:
    node = tracker[node]
    path = [node] + path

print('최소 경로 :', *(n for n in path), sep=' ')
