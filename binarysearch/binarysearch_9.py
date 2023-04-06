"""
프로그래머스 - 징검다리
"""


def solution(distance, rocks, n):
    rocks.sort()

    rocks.append(distance)
    right = distance
    left = 0

    while left < right:
        mid = (right + left) // 2
        remove_cnt = 0
        prev = 0
        for i in range(len(rocks)):
            if rocks[i] - prev < mid:
                remove_cnt += 1
            else:
                prev = rocks[i]

            if remove_cnt > n:
                break

        if remove_cnt <= n:
            left = mid + 1
        else:
            right = mid

    return left - 1


if __name__ == "__main__":
    distance = 25
    rocks = [2, 14, 11, 21, 17]
    n = 2
    print(solution(distance, rocks, n))
