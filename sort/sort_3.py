### 정렬 - 가장 큰 수
# 0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내라.
# 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210 이다.
# 0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때,
# 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return
# [제한 사항]
# 1 <= numbers 길이 <= 100,000
# 0 <= numbers 원소 <= 1,000
###

def solution(numbers):
  numbers = [str(x) for x in numbers]
  numbers.sort(key=lambda x : (x * 4)[:4], reverse=True)
  if numbers[0] == '0':
    answer = '0'
  else:
    answer = ''.join(numbers)
  return answer