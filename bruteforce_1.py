import sys


def solution():
    # n <= 1000
    n = int(sys.stdin.readline())
    
    if n < 100:
        return n

    # n >= 101
    total = 0
    while n >= 1:
        diff = None
        is_diff = True
        str_n = str(n)
        for i, _ in enumerate(str_n):
            if len(str_n) - 1 > i:
                d = int(str_n[i+1]) - int(str_n[i])

                if diff is None:
                        diff = d
                else:
                    if diff != d:
                        is_diff = False
                        break

        if is_diff is True:
            total += 1

        n -= 1
    
    return total
            

print(solution())