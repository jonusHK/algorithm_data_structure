### 탐욕법 - 큰 수 만들기
# 어떤 숫자에서 k개의 수를 제거했을 때, 얻을 수 있는 가장 큰 숫자를 구하라.
# 1924에서 수 두개를 제거하면 [19, 12, 14, 92, 94, 24]를 만들 수 있고 이 중 가장 큰 숫자는 94이다.
# 문자열 형식으로 된 숫자 number에서 k개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return
###

def solution(number, k):
  # number = "4177252841", k = 4
  collected = []
  for i, num in enumerate(number):
    while len(collected) > 0 and collected[-1] < num and k > 0:
      collected.pop()
      k -= 1
    if k == 0:
      collected += list(number[i:])
      break
    collected.append(num)
  collected = collected[:-k] if k > 0 else collected
  answer = ''.join(collected)
  # answer = "775841"
  return answer
