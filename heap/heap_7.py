"""
프로그래머스 - 디스크 컨트롤러
"""


import heapq


def solution(jobs):
    len_jobs = len(jobs)
    jobs.sort()

    q = []
    total = 0
    visited = [0] * len_jobs
    now = 0

    heapq.heapify(q)

    while q or visited[-1] == 0:
        for i, job in enumerate(jobs):
            if visited[i] == 1:
                continue
            if job[0] > now:
                break
            heapq.heappush(q, [job[1], job[0]])
            visited[i] = 1

        if q:
            time, req = heapq.heappop(q)
            now += time
            total += now - req
        else:
            now += 1

    return int(total // len_jobs)


if __name__ == "__main__":
    jobs = [[0, 3], [1, 9], [2, 6], [4, 1], [10, 1]]
    print(solution(jobs))
