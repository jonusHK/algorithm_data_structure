"""
백준 - 꽃길
"""

from itertools import product, combinations
from typing import Tuple, List


def validated(_comb: Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]):
    checked = list(_comb)
    for _coord in _comb:
        for i in range(4):
            x, y = _coord[0] + dx[i], _coord[1] + dy[i]
            if x < 0 or x >= n or y < 0 or y >= n:
                return False, None
            checked.append((x, y))

    if len(checked) != len(set(checked)):
        return False, None

    return True, checked


def sum_val(_coords: List[Tuple[int, int]]):
    _sum = 0
    for _coord in _coords:
        _sum += mapping[_coord[0]][_coord[1]]
    return _sum


n = int(input())
mapping: List[List[int]] = [list(map(int, input().split())) for _ in range(n)]

range_idx: List[int] = [i for i in range(1, n - 1)]
coords: List[Tuple[int, int]] = list(product(*[range_idx, range_idx]))
combs: List[Tuple[Tuple[int, int], Tuple[int, int], Tuple[int, int]]] = list(combinations(coords, 3))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

min_val = 3000
for comb in combs:
    is_valid, validated_coords = validated(comb)
    if is_valid:
        min_val = min(min_val, sum_val(validated_coords))

print(min_val)
