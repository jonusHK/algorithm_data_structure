"""
백준 - 뒤집기
"""

s = str(input())

counts = [0, 0]
for i, v in enumerate(s):
    if i == 0:
        counts[int(v)] = 1
        continue
    if s[i-1] != s[i]:
        counts[int(v)] += 1

print(min(counts))
