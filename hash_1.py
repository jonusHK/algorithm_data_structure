# 완주하지 못한 선수 찾기

def solution(participant, completion):
  d = {}
  for x in participant:
    d[x] = d.get(x, 0) + 1
  for x in completion:
    d[x] -= 1
  dnf = [k for k, v in d.items() if v > 0]
  answer = dnf[0]
  return answer

participant = ["jace", "jonus"]
completion = ["jonus"]

print(solution(participant, completion))