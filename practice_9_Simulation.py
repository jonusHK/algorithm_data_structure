### 시뮬레이션 - 기둥과 보 설치
# 기둥은 바닥 위, 보의 한쪽 끝 부분 위, 다른 기둥 위에만 설치 가능
# 보는 한쪽 끝 부분이 기둥 위, 양쪽 끝 부분이 다른 보와 동시에 연결되면 설치 가능
# 기둥과 보를 설치 및 삭제하는 명령이 담긴 build_frame을 이용하여 n x n 크기의 board 벽면을 벗어나지 않도록 설치된 기둥과 보의 좌표를 return
# build_frame = [[x, y, a, b], ...] -> x, y = 좌표, a = 0은 기둥, 1은 보, b = 0은 삭제, 1은 생성
# answer = [[x, y, a], ...]
# x 기준으로 오름차순 정렬 (x가 같다면 y 기준 정렬)
###

def possible(answer):
    for x, y, stuff in answer:
        if stuff == 0:
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif stuff == 1:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True

def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, stuff, operate = frame
        if operate == 0:
            answer.remove([x, y, stuff])
            if not possible(answer):
                answer.append([x, y, stuff])
        if operate == 1:
            answer.append([x, y, stuff])
            if not possible(answer):
                answer.remove([x, y, stuff])
    return sorted(answer)


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))