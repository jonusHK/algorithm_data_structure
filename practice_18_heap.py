import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    min_val = heapq.heappop(scoville)
    cnt = 0
    while min_val < K:
        if len(scoville) == 0:
            return -1
        new_val = min_val + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_val)
        cnt += 1
        min_val = heapq.heappop(scoville)

    return cnt

print(solution([1, 2, 3, 9, 10, 12], 7))