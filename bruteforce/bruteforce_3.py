### 완전탐색 - 문자열 압축
# 문자열에서 같은 값이 연속해서 나타나는 것을 그 문자의 개수와 반복되는 값으로 표현하여 더 짧은 문자열로 줄여서 표현
# 예를 들어, "abcabcdede"의 경우, 문자를 2개 단위로 잘라서 압축하면 "abcabc2de"가 되지만, 
# 3개 단위로 자르면 "2abcdede"가 되어, 3개 단위가 가장 짧은 압축 방법이 된다.
# 압축할 문자열 s가 매개변수로 주어질 때, 1개 이상 단위로 문자열을 잘라 압축하여 표현할 문자열 중 가장 짧은 것의 길이를 return
###

def solution(s):
    answer = len(s)
    for step in range(1, len(s)):
        compressed = ""
        prev = s[0:step]
        count = 1
        for j in range(step, len(s), step):
            if prev == s[j:j + step]:
                count += 1
            else:
                compressed += str(count) + prev if count >= 2 else prev
                prev = s[j:j + step]
                count = 1
        compressed += str(count) + prev if count >= 2 else prev
        answer = min(answer, len(compressed))
    return answer

print(solution("ababcdcdababcdcd"))