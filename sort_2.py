# 계수 정렬(Counting Sort) 적용
# 데이터 개수가 많을 때 파이썬에서는 sys.stdin.readline() 사용
# 메모리 제한이 8MB로 주어졌기 때문에, Pypy3 가 아닌 Python3 로 제출해야 함 (Pypy3은 시간은 빠르나 메모리를 많이 사용함)
import sys

N = int(sys.stdin.readline())

rst = [0] * 10001
for _ in range(N):
    num = int(sys.stdin.readline())
    rst[num] += 1


for i in range(10001):
    if rst[i] != 0:
        for _ in range(rst[i]):
            print(i)


