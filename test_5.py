from bisect import bisect_right


def solution(A):
    try:
        A.sort()    
        if A[0] >= 0:
            return 0

        max_idx = bisect_right(A, -A[0]) - 1
        min_idx = bisect_right(A, 0)
        max_num = 0
        for idx in range(max_idx, min_idx, -1):
            neg_idx = bisect_right(A, -A[idx]) - 1
            if A[neg_idx] + A[idx] == 0:
                max_num = A[idx]
                break
        return max_num
    except Exception as e:
        raise e
    
    
print(solution([-5, -3, -2, -1, 1, 2, 3, 5]))
