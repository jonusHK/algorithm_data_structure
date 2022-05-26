n, m = map(int, input().split())

positions = list(map(int, input().split()))
positions.append(0)
positions.sort()

left = []
right = []
for position in positions:
    if position >= 0:
        right.append(position)
    else:
        left.append(position)

cnt = 0
left_ptr, right_ptr = 0, len(right) - 1
left_bigger, right_bigger = False, False

if left:
    if abs(left[left_ptr]) >= abs(right[right_ptr]):
        left_bigger = True
    else:
        right_bigger = True
else:
    right_bigger = True

while right_ptr >= 0:
    if right_bigger and right_ptr == len(right) - 1:
        cnt += right[right_ptr]
    else:
        cnt += right[right_ptr] * 2
    right_ptr -= m

if left:
    while left_ptr < len(left):
        if left_bigger and left_ptr == 0:
            cnt += abs(left[left_ptr])
        else:
            cnt += abs(left[left_ptr] * 2)
        left_ptr += m

print(cnt)
