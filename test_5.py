from bisect import bisect_right


def solution(array):
    try:
        array.sort()
        if array[0] >= 0:
            return 0

        max_idx = bisect_right(array, -array[0]) - 1
        min_idx = bisect_right(array, 0)
        max_num = 0
        for idx in range(max_idx, min_idx, -1):
            neg_idx = bisect_right(array, -array[idx]) - 1
            if array[neg_idx] + array[idx] == 0:
                max_num = array[idx]
                break
        return max_num
    except Exception as e:
        raise e
    
    
print(solution([-5, -3, -2, -1, 1, 2, 3, 5]))
