import sys


def solution():
    n = int(sys.stdin.readline())
    li = list(map(int, sys.stdin.readline().split()))

    li.sort()

    result1 = 0
    for idx1, _ in enumerate(li):
        result2 = 0
        for idx2 in range(idx1 + 1):
            result2 += li[idx2]
        
        result1 += result2
    
    print(result1)

solution()