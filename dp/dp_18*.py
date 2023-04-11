"""
프로그래머스 - 연속 펄스 부분 수열의 합
"""


def solution(sequence):
    sequence_len = len(sequence)
    dp = [[0] * sequence_len for _ in range(2)]
    pulse = ((1, -1), (-1, 1))

    for i in range(2):
        dp[i][0] = sequence[0] * pulse[i][0]
        for j in range(1, sequence_len):
            cur_val = sequence[j] * pulse[i][j % 2]
            dp[i][j] = max(dp[i][j-1] + cur_val, cur_val)

    return max([max(dp[i]) for i in range(2)])


if __name__ == '__main__':
    sequence = [2, 3, -6, 1, 3, -1, 2, 4]
    print(solution(sequence))
