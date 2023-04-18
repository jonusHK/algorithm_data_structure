def solution(A):
    A.sort()
    prev, diff = -1, 10 ** 9
    for a in set(A):
        if prev != -1:
            diff = min(diff, a - prev)
        prev = a
    return diff


if __name__ == "__main__":
    A = [9, 11, 7]
    print(solution(A))
