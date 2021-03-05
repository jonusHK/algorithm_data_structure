### 완주하지 못한 선수 찾기
# 단 한명의 선수 제외하고 모든 선수가 마라톤 완주
# 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때,
# 완주하지 못한 선수의 이름을 return
###

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