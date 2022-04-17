n = int(input())

dic = {}
for _ in range(n):
    name = input()
    dic[name] = dic.get(name, 0) + 1

rst = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

print(rst[0][0])
