import sys


def find_max(li, rem):
    max_val = None
    for idx, val in enumerate(li):
        if val > rem:
            max_idx = idx - 1
            max_val = li[max_idx]
            break
        
    if max_val is None:
        max_idx = len(li) - 1
        max_val = li[max_idx] 
    
    return max_idx, max_val


def solution():
    n, k = map(int, sys.stdin.readline().split())

    coin_val_li = []
    for _ in range(n):
        coin_val_li.append(int(sys.stdin.readline()))

    coin_val_li.sort()

    cnt, rem, li = 0, k, coin_val_li

    try:
        while True:
            max_idx, max_val = find_max(li, rem)
            cnt += rem // max_val
            rem = rem % max_val

            if rem == 0:
                break
            
            if max_idx == 0:
                raise Exception('해당 동전 가치로 k를 만들 수 없습니다.')
        
            li = li[:max_idx]

    except Exception as e:
        return e


    return cnt

print(solution())
