"""
백준 - 센서

이진탐색으로 풀 경우 반례는 아래와 같다.
n = 7
k = 3
1 2 3 4 6 7 8
"""


n = int(input())
k = int(input())

sensors = list(set(map(int, input().split())))
sensors.sort()

st = 1000000
for i in range(len(sensors) - 1):
    st = min(sensors[i+1] - sensors[i], st)
ed = sensors[-1] - sensors[0]

sensors_pos = [False] * 1000001
for i in sensors:
    sensors_pos[i] = True

min_distance = 1000000
while st <= ed:
    mid = (st + ed) // 2
    offset = sensors[0]
    cnt = 0
    distance = 0
    all_checked = False
    while cnt < k:
        next_sensor_idx = offset
        cnt += 1
        next_idx = offset + mid
        if next_idx > sensors[-1]:
            next_idx = sensors[-1]
        for idx in range(offset + 1, next_idx + 1):
            if sensors_pos[idx]:
                next_sensor_idx = idx
        distance += (next_sensor_idx - offset)

        if next_sensor_idx == sensors[-1]:
            all_checked = True
            break

        for idx, val in enumerate(sensors_pos[next_sensor_idx+1:]):
            if val:
                offset = next_sensor_idx + 1 + idx
                break

    if not all_checked:
        st = mid + 1
    else:
        min_distance = min(min_distance, distance)
        ed = mid - 1

print(min_distance)
