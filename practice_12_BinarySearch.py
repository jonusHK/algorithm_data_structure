### 이진 탐색 - 예산
#  정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음과 같이 배정한다.
# 1. 모든 요청이 배정될 수 있다면 요청 금액 그대로 배정
# 2. 모든 요청이 배정될 수 없다면 상한액 계산하여 그 이상 예산요청에는 모두 상한액 배정 (상한액 이하 예산요청에는 요청 금액 그대로 배정)
# 예를 들어, 전체 국가예산이 485이고 4개 지방의 예산요청이 각각 120, 110, 140, 150일 때, 상한액 127로 잡으면, 
# 120, 110, 127, 127을 배정하고 그 합이 484로 가능한 최대가 된다.
# 각 요청 예산이 담긴 배열 budgets과 총 예산 M이 매개변수로 주어질 때, 최대 상한액 return
###

def solution(budgets, M):
    answer = 0
    start = 0 
    end = max(budgets)

    while start <= end:
        mid = (end + start) // 2
        money = 0
        for budget in budgets:
            money += min(mid, budget)
        if money <= M:
            answer = mid
            start = mid + 1
    return answer

