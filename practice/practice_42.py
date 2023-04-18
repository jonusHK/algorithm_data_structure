def solution(A):
    A.sort()

    left = 1
    right = A[-1] - A[0]

    while left < right:
        mid = (left + right) // 2

        sep_idx = 0
        sep_num = A[0] + mid
        for i in range(len(A)):
            if A[i] <= sep_num:
                continue

            sep_idx = i
            break

        if A[-1] - A[sep_idx] > mid:
            left = mid + 1
        else:
            right = mid

    return left


if __name__ == "__main__":
    # A = [0, 44, 32, 30, 42, 18, 34, 16, 35]
    A = [11, 20, 15]
    print(solution(A))
