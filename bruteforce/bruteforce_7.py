"""
프로그래머스 - 모음사전
"""

string = "AEIOU"
result_cnt = 0
stop = False


def dfs(word: str, cnt: int = 0, w: str = ""):
    global result_cnt, stop

    if word == w:
        stop = True
        return

    if cnt == 5:
        return w

    for s in string:
        if stop:
            break
        result_cnt += 1
        dfs(word, cnt + 1, w + s)


def solution(word):
    dfs(word)
    return result_cnt


print(solution("I"))
