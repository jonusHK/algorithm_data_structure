import heapq

n = int(input())

input_li = []
heap = []
for _ in range(n):
    input_li.append(int(input()))

for num in input_li:
    if num == 0:
        if heap:
            min_num = heapq.heappop(heap)
            print(min_num)
        else:
            print(0)
    else:
        heapq.heappush(heap, num)
