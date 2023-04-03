"""
프로그래머스 - 단어 변환
"""

from collections import deque
from typing import List


def get_next(cur: str, words: List[str]):
    for w in words:
        if w == cur:
            continue

        if sum([x != y for x, y in zip(w, cur)]) == 1:
            yield w


def bfs(begin: str, target: str, words: List[str]):
    dist = {
        begin: 0
    }
    q = deque([begin])

    while q:
        word = q.pop()
        if word == target:
            break

        for w in get_next(word, words):
            if w in dist:
                continue
            dist[w] = dist[word] + 1
            q.append(w)

    return dist.get(target, 0)


def solution(begin, target, words):
    return bfs(begin, target, words)


if __name__ == '__main__':
    begin = "hit"
    target = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(begin, target, words))
