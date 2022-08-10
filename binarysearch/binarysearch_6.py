### 이진 탐색 - 가사 검색
# 노래 가사에 사용된 단어들 중에 특정된 키워드가 몇 개 포함되어 있는지 프로그램으로 개발
# 와일드카드 문자인 '?'는 글자 하나를 의미하며, 어떤 문자에도 매치된다고 가정
# 예를 들어, "fro?"는 "frodo", "front", "frost" 등에 매치되지만 "frame", "frozen"에는 매치되지 않는다.
# 가사에 사용된 모든 단어들이 담긴 배열 words 와 찾고자 하는 키워드가 담긴 배열 queries 가 주어질 때,
# 각 키워드 별로 매치된 단어가 몇 개인지 순서대로 배열에 담아 return
###

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

# 모든 단어들을 길이마다 나누어서 저장하기 위한 리스트
data = [[] for _ in range(10001)]
# 모든 단어들을 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_data = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        data[len(word)].append(word)
        reversed_data[len(word)].append(word[::-1])
    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어들 정렬 수행
        data[i].sort()
        reversed_data[i].sort()

    for q in queries: # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?': # 접미사에 와일드 카드가 붙은 경우
            res = count_by_range(data[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 접두사에 와일드 카드가 붙은 경우
            res = count_by_range(reversed_data[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        # 검색된 단어의 개수를 저장
        answer.append(res)
    return answer