import copy
import sys

string = sys.stdin.readline().rstrip()
keyword = sys.stdin.readline().rstrip()

max_cnt = 0
idx = 0

for i in range(len(string)):
    copied_str = copy.copy(string[i:])
    cnt = 0
    while True:
        start_idx = copied_str.find(keyword)
        if start_idx != -1:
            cnt += 1
            if len(copied_str) == start_idx + len(keyword):
                break
            copied_str = copied_str[start_idx + len(keyword):]
        else:
            break

    max_cnt = max(max_cnt, cnt)

print(max_cnt)
