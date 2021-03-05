### 동적계획법 - N으로 표현
# number를 N을 이용하여 만들 때, N이 사용되는 최소값 리턴
# ex) 12 = 5 + 5 + 5/5 + 5/5 (6번)
#     12 = 55 / 5 + 5 / 5 (5번)
#     12 = (55 + 5) / 5 (4번)
#     --> return 4 (최솟값이 8보다 크면 return -1)
# N = 5
# 1번 - 5
# 2번 - 55 10 0 25 1
# 3번 - 555 60 15 5 30 6 -50 -5 -20 4 275 50 0 125 11 2 20 -4
# 4번 - 5555, 1번 (+ - * /) 3번, 2번 (+ - * /) 2번, 3번 (+ - * /) 1번
###

def solution(N, number):
  # s = [{5}, {55, ...}, {555, ...}, ... , {55555555, ...}]
  s = [set() for x in range(8)]
  for i, x in enumerate(s, start=1):
    x.add(int(str(N) * i))
    if i == 0 and number == x:
      return 1

  for i in range(1, len(s)):
    for j in range(i):
      for op1 in s[j]:
        for op2 in s[i - j - 1]:
          s[i].add(op1 + op2)
          s[i].add(op1 - op2)
          s[i].add(op1 * op2)
          if op2 != 0:
            s[i].add(op1 // op2)
    if number in s[i]:
      answer = i + 1
      break
  # for문에서 break 없이 빠져나온 경우
  else:
    answer = -1
  
  return answer

print(solution(5, 12))