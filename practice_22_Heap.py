### 힙 - 이중우선순위큐
# operations	               return
# ["I 16","D 1"]	            [0,0]
# ["I 7","I 5","I -5","D -1"]	[7,5]
###
import heapq


def solution(operations):
    min_heap = []
    heapq.heapify(min_heap)

    for op in operations:
        command, num = op.split()
        num = int(num)

        # 'I 숫자' 인 경우
        if command == 'I':
            heapq.heappush(min_heap, num)
        # 'D 1' 인 경우
        elif num == 1:
            if min_heap:
                min_heap.pop(min_heap.index(heapq.nlargest(1, min_heap)[0]))
        # 'D -1' 인 경우
        else:
            if min_heap:
                heapq.heappop(min_heap)
    
    if min_heap:
        return [heapq.nlargest(1, min_heap)[0], heapq.nsmallest(1, min_heap)[0]]
    else:
        return [0, 0]

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
