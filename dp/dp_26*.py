"""
프로그래머스 - 광고 삽입
"""


def time_to_sec(target):
    hour, minute, second = map(int, target.split(':'))
    return hour * 3600 + minute * 60 + second


def sec_to_time(second):
    m, s = divmod(second, 60)
    h, m = divmod(m, 60)
    return f"{str(h).rjust(2, '0')}:{str(m).rjust(2, '0')}:{str(s).rjust(2, '0')}"


def solution(play_time, adv_time, logs):
    play_sec = time_to_sec(play_time)
    adv_sec = time_to_sec(adv_time)

    times = [0] * (play_sec + 1)

    for log in logs:
        start, end = map(lambda x: time_to_sec(x), log.split('-'))
        times[start] += 1
        times[end] -= 1

    for i in range(1, len(times)):
        times[i] += times[i-1]

    for i in range(1, len(times)):
        times[i] += times[i-1]

    max_view = times[adv_sec-1]
    max_sec = 0
    for i in range(adv_sec, play_sec):
        view = times[i] - times[i-adv_sec]
        if max_view < view:
            max_view = view
            max_sec = i - adv_sec + 1

    return sec_to_time(max_sec)


if __name__ == "__main__":
    play_time = "02:03:55"
    adv_time = "00:14:15"
    logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
    print(solution(play_time, adv_time, logs))
