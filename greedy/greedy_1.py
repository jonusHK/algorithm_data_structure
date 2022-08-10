import sys


def solution():
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))

    li.sort()

    result = 0
    for idx1 in range(n):
        for idx2 in range(idx1 + 1):
            result += li[idx2]
    
    return result

print(solution())
