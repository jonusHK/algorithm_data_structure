# 이진 탐색 - 징검다리

def solution(distance, rocks, n):
    rocks.sort()
    left = 1
    right = distance
    answer = 1

    while left <= right:
        mid = (left + right) // 2
        removeCnt = 0
        prev = 0
        for i in range(len(rocks)):
            if i == len(rocks) - 1:
                if rocks[i] - prev < mid or distance - rocks[i] < mid:
                    removeCnt += 1
            else:
                if rocks[i] - prev < mid:
                    removeCnt += 1
                else:
                    prev = rocks[i]

            if removeCnt > n:
                break

        if removeCnt > n:
            right = mid - 1
        else:
            answer = answer if answer > mid else mid
            left = mid + 1

    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))
