"""
프로그래머스 - 기둥과 보 설치
"""


def is_valid(x, y, a, result):
    # 기둥
    if a == 0:
        if y == 0 or [x, y-1, 0] in result or [x, y, 1] in result or [x-1, y, 1] in result:
            return True

    # 보
    else:
        if [x, y-1, 0] in result or [x+1, y-1, 0] in result or ([x-1, y, 1] in result and [x+1, y, 1] in result):
            return True

    return False


def solution(n, build_frame):
    result = []
    for x, y, a, b in build_frame:
        # 건물 생성
        if b == 1:
            if is_valid(x, y, a, result):
                result.append([x, y, a])

        # 건물 제거
        else:
            result.remove([x, y, a])
            for i in result:
                _x, _y, _a = i
                if not is_valid(_x, _y, _a, result):
                    result.append([x, y, a])
                    break

    answer = sorted(result)
    return answer


if __name__ == "__main__":
    n = 5
    build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
    print(solution(n, build_frame))
