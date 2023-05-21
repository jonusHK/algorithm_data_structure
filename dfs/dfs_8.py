"""
프로그래머스 - 혼자 놀기의 달인
"""


def dfs(i, cards, visited):
    cnt = 0
    if visited[i]:
        return cnt

    stack = [cards[i]]
    visited[i] = 1
    cnt += 1

    while stack:
        idx = stack.pop()
        if visited[idx]:
            break

        stack.append(cards[idx])
        visited[idx] = 1
        cnt += 1

    return cnt


def solution(cards):
    cards.insert(0, 0)
    visited = [0] * len(cards)
    results = []

    for i in range(1, len(cards)):
        results.append(dfs(i, cards, visited))

    results.sort(reverse=True)
    if results[0] == len(cards):
        return 0

    return results[0] * results[1]


if __name__ == "__main__":
    cards = [8, 6, 3, 7, 2, 5, 1, 4]
    print(solution(cards))
