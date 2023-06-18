"""
프로그래머스 - 과제 진행하기
"""


from collections import deque


def convert_to_minute(time):
    return int(time[:2]) * 60 + int(time[3:])


def solution(plans):

    plans = sorted(map(lambda x: [x[0], convert_to_minute(x[1]), int(x[2])], plans), key=lambda x: x[1])

    stopped = []
    finished = deque([])

    for i in range(1, len(plans)):
        diff = plans[i][1] - plans[i-1][1] - plans[i-1][2]
        if diff < 0:
            stopped.append((plans[i-1][0], diff * -1))
        else:
            finished.append(plans[i-1][0])

            while stopped and diff > 0:
                recent_stopped = stopped.pop()
                diff -= recent_stopped[1]
                if diff < 0:
                    stopped.append((recent_stopped[0], diff * -1))
                else:
                    finished.append(recent_stopped[0])

    finished.append(plans[-1][0])

    while stopped:
        finished.append(stopped.pop()[0])

    answer = []
    while finished:
        answer.append(finished.popleft())

    return answer


if __name__ == "__main__":
    plans = [["aaa", "12:00", "20"], ["bbb", "12:10", "30"], ["ccc", "12:40", "10"]]
    print(solution(plans))
