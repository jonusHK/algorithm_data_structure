d = int(input())

"""
0: 정보과학관 
1: 전산관
2: 미래관 
3: 신양관
4: 한경직기념관
5: 진리관
6: 학생회관
7: 형남공학관
"""

mapping = [
    (1, 2),
    (0, 2, 3),
    (0, 1, 3, 4),
    (1, 2, 4, 5),
    (2, 3, 5, 7),
    (3, 4, 6),
    (5, 7),
    (4, 6)
]

dp = [[0] * (len(mapping) + 1) for _ in range(d + 1)]
dp[0][0] = 1

for i in range(d):
    for j in range(len(mapping) + 1):
        if dp[i][j] >= 1:
            for v in mapping[j]:
                dp[i+1][v] = (dp[i+1][v] + dp[i][j]) % 1000000007

print(dp[d][0])
