def get_price():
    case = list(map(int, input().split()))
    dic = {}
    for num in case:
        if dic.get(num):
            dic[num] += 1
        else:
            dic[num] = 1

    if len(dic) == 1:
        return 50000 + next(iter(dic)) * 5000
    elif len(dic) == 2:
        for target, cnt in dic.items():
            if cnt == 3:
                return 10000 + target * 1000
            elif cnt == 2:
                other = next((_k for _k in dic.keys() if _k != target), None)
                if other:
                    return 2000 + target * 500 + other * 500
    elif len(dic) == 3:
        target = next((_k for _k, _v in dic.items() if _v == 2), None)
        if target:
            return 1000 + target * 100
    else:
        return max(dic.keys()) * 100

    raise RuntimeError('Not valid.')


n = int(input())

print(max(get_price() for i in range(n)))
