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