import heapq

### 힙 - 스코빌 지수 K 이상 만들기
# 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두번째로 맵지 않은 음식의 스코빌 지수 * 2)
# 모든 음식의 지수가 K 이상이 될 때까지 반복하여 섞는다.
# 음식의 스코빌 지수를 담은 배열 scoville과 원하는 스코빌 지수 K가 주어질 때,
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return
###

def solution(scoville, K):
  answer = 0
  heapq.heapify(scoville) # min heap 구성
  while True:
    min1 = heapq.heappop(scoville)
    if min1 >= K:
      break
    elif len(scoville) == 0:
      answer = -1
      break
    min2 = heapq.heappop(scoville)
    new_scoville = min1 + 2 * min2
    heapq.heappush(scoville, new_scoville)
    answer += 1
    
  return answer

  
