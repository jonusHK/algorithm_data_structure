### 너비 우선 탐색 (BFS) - 단어 변환
# begin, target과 단어의 집합 word가 있다. begin에서 target으로 변환하는 가장 짧은 변화 과정을 찾으려고 한다.
# 한번에 한개의 알파벳만 바꿀 수 있고, words에 있는 단어로만 변환이 가능하다고 한다.
# 예를 들어, begin이 'hit', target이 'cog', words가 ['hot', 'dot', 'dog', 'lot', 'log', 'cog']라면,
# 'hit' -> 'hot' -> 'dot' -> 'dog' -> 'cog' 와 같이 4단계를 거쳐 변환 가능하다.
# 두 개의 단어 begin, target과 단어의 집합 words가 매개변수로 주어질 때, 최소 몇 단계의 과정을 거쳐 begin을 target으로 변환할 수 있는지 return
###

from collections import deque

# 단어를 변환할 수 있는 경우 (1개 이하의 알파벳만 다른 경우)
def possible(begin, target):
    length = len(begin)
    count = 0 # 다른 알파벳의 개수
    for i in range(length):
        # 두 알파벳이 서로 다를 때마다 카운트
        if begin[i] != target[i]:
            count += 1
        if count == 2: # 알파벳이 2개 이상 다르다면 거짓(False) 반환
            return False

def solution(begin, target, words):
    visited = {begin: 0} # 특정 단어로의 최소 변환 횟수 기록
    # 너비 우선 탐색(BFS) 시작
    q = deque([begin])
    while q:
        now = q.popleft()
        for word in words:
            if word not in visited and possible(now, word):
                visited[word] = visited[now] + 1
                q.append(word)
    # 목표 단어로 변환이 가능하다면 최소 변환 횟수 출력
    if target in visited:
        return visited[target]
    return 0
