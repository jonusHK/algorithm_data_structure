nums = list(map(int, input().split()))

dic = {}
for n in nums:
    if dic.get(n):
        dic[n] += 1
    else:
        dic[n] = 1

if len(dic) == 3:
    print(max(dic.keys()) * 100)
elif len(dic) == 2:
    for k, v in dic.items():
        if v == 2:
            print(1000 + k * 100)
else:
    print(10000 + next(iter(dic)) * 1000)
