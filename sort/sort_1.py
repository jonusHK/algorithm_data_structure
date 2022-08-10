N = int(input())

rst = []
for _ in range(N):
    age, name = input().split(' ')
    rst.append((int(age), name))

rst.sort(key=lambda x: x[0])

for v in rst:
    print(v[1], v[2])
