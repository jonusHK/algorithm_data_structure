from collections import deque
import copy

def check_li(li):
    for val in li:
        if val != 0:
            return False
    return True

def next_pos(li, idx, cnt):
    rst = []
    cnt += 1
    
    cnt_1 = li[idx - 1]
    li_1 = copy.deepcopy(li)
    li_1[idx - 1] = 0

    cnt_2 = li[idx + 1]
    li_2 = copy.deepcopy(li)
    li_2[idx + 1] = 0

    rst.append((li_1, idx - 1, cnt + cnt_1))
    rst.append((li_2, idx + 1, cnt + cnt_2))
    return rst

def solution(name):
    cnt_li = []
    for alp in name:
        cnt_li.append(min(ord('Z') - ord(alp) + 1, ord(alp) - ord('A')))
    
    first_cnt = cnt_li[0]
    cnt_li[0] = 0
    q = deque([(cnt_li, 0, first_cnt)])

    while len(q) > 0:
        pop_li, pop_idx, pop_cnt = q.popleft()

        for pos in next_pos(copy.deepcopy(pop_li), pop_idx, pop_cnt):
            next_li, next_idx, _ = pos
            if (next_idx == len(next_li)) or (next_idx < -len(next_li)):
                continue
            else:
                q.append(pos)

        if check_li(pop_li) == True:
            return pop_cnt

    return -1

print(solution('BBABAAAB'))