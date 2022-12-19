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


def dijkstra(start_n: str):
    tracker = {k: k for k in mapping.keys()}
    distance = {k: inf_num for k in mapping.keys()}
    distance[start_n] = 0
    q = [(0, start_n)]
    heapq.heapify(q)

    while q:
        w, n = heapq.heappop(q)
        for _n, _w in mapping[n]:
            new_w = distance[n] + _w
            if distance[_n] > new_w:
                distance[_n] = new_w
                tracker[_n] = n
                heapq.heappush(q, (new_w, _n))

    path = [end_node]
    ptr = end_node
    while tracker[ptr] != ptr:
        ptr = tracker[ptr]
        path = [ptr] + path

    return distance[end_node], path


print(dijkstra(start_node))
