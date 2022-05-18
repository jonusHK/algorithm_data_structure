"""
백준 - 뒤집기
"""

words = str(input())

counts = [0, 0]
for idx, val in enumerate(words):
    if idx == 0:
        counts[int(val)] = 1
        continue

    if words[idx - 1] != words[idx]:
        counts[int(val)] += 1

print(min(counts[0], counts[1]))
