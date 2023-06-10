"""
프로그래머스 - [1차] 셔틀버스
"""


from collections import deque

START_TIME = "09:00"
MAX_NUMBER = 10
MAX_INTERVAL = 60


def calc_time(time, dt):
    hour = int(time[:2])
    minute = int(time[3:])

    dh, dm = divmod(dt, 60)
    _dh, nm = divmod(minute + dm, 60)
    nh = (hour + dh + _dh) % 24

    return f"{str(nh).rjust(2, '0')}:{str(nm).rjust(2, '0')}"


def solution(n, t, m, timetable):
    max_time = calc_time(START_TIME, (MAX_NUMBER-1) * MAX_INTERVAL)
    timetable = [time for time in timetable if time <= max_time]
    ideal_time = calc_time(START_TIME, (n-1) * t)

    if not timetable:
        return ideal_time

    timetable.sort()

    q = deque(timetable)
    for i in range(n):
        end_time = calc_time(START_TIME, i * t)

        cnt = 0
        while q and cnt < m:
            if q[0] > end_time:
                break

            time = q.popleft()
            cnt += 1

            if i == n - 1 and cnt == m:
                return calc_time(time, -1)

    return ideal_time


if __name__ == "__main__":
    n, t, m = 1, 1, 5
    timetable = ["08:00", "08:01", "08:02", "08:03"]
    print(solution(n, t, m, timetable))
