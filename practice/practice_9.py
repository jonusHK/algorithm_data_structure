from copy import deepcopy
from typing import List

l, c = map(int, input().split())
words = input().split()
words.sort()
results = []


def validate(case: List[str]):
    m = set(case)
    n = {'a', 'e', 'i', 'o', 'u'}
    return len(m & n) >= 1 and len(m - n) >= 2


def dfs(idx: int, word: str, case: List[str]):
    case.append(word)
    if len(case) == l:
        if validate(case):
            results.append(deepcopy(case))
        return

    for _i, _v in enumerate(words[idx+1:]):
        next_idx = idx + _i + 1
        dfs(next_idx, _v, case)
        case.pop(-1)


for i, v in enumerate(words):
    dfs(i, v, [])

for r in results:
    print(''.join(r))
