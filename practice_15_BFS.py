### 너비 우선 탐색 - 블록 이동하기
# '0'과 '1'로 이루어진 N x N 크기의 지도에서 2 x 1 크기의 로봇을 움직여 (N, N) 위치까지 이동 할 수 있도록 프로그래밍을 하려고 한다.
# 로봇이 이동하는 지도는 가장 왼쪽, 상단의 좌표를 (1, 1)로 하며 지도 내에 표시된 숫자 '0'는 빈칸을 '1'은 벽을 나타낸다.
# 로봇은 벽이 있는 칸 또는 지도 밖으로는 이동할 수 없으며, 회전은 가능하다. (회전하는 방향에 벽이 있으면 안됨)
# '0'과 '1'로 이루어진 지도인 board가 주어질 때, 로봇이 (N, N) 위치까지 이동하는데 필요한 시간을 return
# 제한사항 : board 한 변의 길이는 5 이상 100 이하 / board 원소는 0 또는 1 / 로봇이 처음에 놓여있는 칸 (1, 1), (1, 2)는 항상 0으로 주어짐 / 로봇이 항상 목적지에 도착할 수 있는 경우만 입력으로 주어짐
###