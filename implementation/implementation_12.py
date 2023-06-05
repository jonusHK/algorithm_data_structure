"""
프로그래머스 - 혼자서 하는 틱택토
"""


def is_valid(mapper, win_o_cnt, win_x_cnt):
    cnt_o = mapper.get("O", 0)
    cnt_x = mapper.get("X", 0)

    if (
        cnt_o < cnt_x
        or cnt_o - cnt_x > 1
        or (win_o_cnt and win_x_cnt)
        or (win_o_cnt == 1 and cnt_o == cnt_x)
        or (win_x_cnt == 1 and cnt_o != cnt_x)
    ):
        return False

    return True


def solution(board):
    mapper = {}

    win_o_cnt, win_x_cnt = 0, 0
    cross_right_v, cross_left_v = '', ''
    cross_right_cnt, cross_left_cnt = 0, 0

    for i in range(3):
        row_v, col_v = '', ''
        row_cnt, col_cnt = 0, 0

        for j in range(3):
            if board[i][j] != '.':
                # 가로 확인
                if row_v == '' or row_v == board[i][j]:
                    row_v = board[i][j]
                    row_cnt += 1

                # 우측 대각선 확인
                if i == j and (cross_right_v == '' or cross_right_v == board[i][j]):
                    cross_right_v = board[i][j]
                    cross_right_cnt += 1

                # 좌측 대각선 확인
                if i + j == len(board) - 1 and (cross_left_v == '' or cross_left_v == board[i][j]):
                    cross_left_v = board[i][j]
                    cross_left_cnt += 1

            if board[j][i] != '.':
                # 세로 확인
                if col_v == '' or col_v == board[j][i]:
                    col_v = board[j][i]
                    col_cnt += 1

            mapper[board[i][j]] = mapper.get(board[i][j], 0) + 1

        for cnt, val in zip(
            [row_cnt, col_cnt, cross_left_cnt, cross_right_cnt],
            [row_v, col_v, cross_left_v, cross_right_v]
        ):
            if cnt == len(board):
                if val == 'O':
                    win_o_cnt += 1
                elif val == 'X':
                    win_x_cnt += 1

    # 유효성 검사
    if is_valid(mapper, win_o_cnt, win_x_cnt):
        return 1

    return 0


if __name__ == "__main__":
    board = ["OOO", "...", "XXX"]
    print(solution(board))
