"""
백준 - LCS (-> 응용하여 가장 긴 길이의 문자열 출력)
"""


from copy import deepcopy
from typing import List, Tuple

n = input()
m = input()

dp: List[List[Tuple[int, Tuple[int, int]]]] = [[(0, (0, 0))] * (len(n) + 1) for _ in range(len(m) + 1)]

for i in range(1, len(n) + 1):
    for j in range(1, len(m) + 1):
        if m[i-1] == n[j-1]:
            dp[i][j]: Tuple[int, Tuple[int, int]] = (dp[i-1][j-1][0] + 1, (i - 1, j - 1))
        else:
            if dp[i-1][j][0] >= dp[i][j-1][0]:
                val = dp[i-1][j][0]
                ref = i - 1, j
            else:
                val = dp[i][j-1][0]
                ref = i, j - 1
            dp[i][j]: Tuple[int, Tuple[int, int]] = val, ref


def get_track(_ref: Tuple[int, int]):
    _track: List[str] = []
    root_ref: Tuple[int, int] = deepcopy(_ref)
    while root_ref != (0, 0):
        cur_i, cur_j = root_ref
        root_ref = dp[cur_i][cur_j][1]
        if root_ref[0] < cur_i and root_ref[1] < cur_j:
            _track.append(n[cur_j-1])
    return _track


tracks = []
max_val = dp[-1][-1]
for i in range(len(dp[-1]) - 1, -1, -1):
    if dp[-1][i] != max_val:
        continue
    track: List[str] = get_track(dp[-1][i][1])
    tracks.append(list(reversed(track)))

print(tracks)
