### 탐욕법 (Greedy) - 체육복
# 체육복이 도난당해, 여벌 체육복이 있는 학생이 이들에게 체육복을 빌려주기로 한다.
# 바로 앞번호의 학생이나 바로 뒷번호의 학생에게만 체육복을 빌려줄 수 있다. (4번 학생은 3번 학생 혹은 5번 학생에게만 체육복을 빌려줄 수 있다.)
# 최대한 많은 학생이 체육수업을 들어야 한다.
# 전체 학생 수 n, 체육복을 도난당한 학생들의 번호가 담긴 배열 lost, 여벌의 체육복을 가져온 학생들의 번호가 담긴 배열 reserve가 매개변수로 주어질 때,
# 체육수업을 들을 수 있는 학생의 최댓값 return
###

def solution1(n, lost, reserve):
  u = [1] * (n + 2)
  for i in reserve:
    u[i] += 1
  for i in lost:
    u[i] -= 1
  for i in range(1, n + 1):
    if u[i - 1] == 0 and u[i] == 2:
      u[i - 1:i + 1] = [1, 1]
    elif u[i] == 2 and u[i + 1] == 0:
      u[i:i + 2] = [1, 1]
  return len([x for x in u[1:-1] if x > 0])

def solution2(n, lost, reserve):
  s = set(lost) & set(reserve) # 교집합
  l = set(lost) - s
  r = set(reserve) - s
  for x in sorted(r):
    if x - 1 in l:
      l.remove(x - 1)
    elif x + 1 in l:
      l.remove(x + 1)
  return n - len(l)


lost = [1, 3, 5]
reserve = [2, 4]
print(solution2(6, lost, reserve))