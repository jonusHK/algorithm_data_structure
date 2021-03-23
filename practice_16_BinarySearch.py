# 이진탐색 - 입국심사

import sys

def solution(n, times):
    answer = sys.maxsize
    left = 0
    right = max(times) * n

    while left <= right:
        done = 0
        mid = (left + right) // 2
        for time in times:
            done += mid // time
        if done < n:
            left = mid + 1
        else:
            answer = min(answer, mid)
            right = mid - 1
    return answer


print(solution(6, [7, 10]))

