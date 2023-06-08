"""
프로그래머스 - 카운트다운
"""

MAX_SCORE = 20
CENTER_SCORE = 50


def solution(target):
    dp = [[1e9, -1] if i > 0 else [0, 0] for i in range(target + 1)]

    for i in range(target):
        for j in range(1, MAX_SCORE + 1):
            for k in range(1, 4):
                score = i + j * k
                if score > target:
                    continue

                if (
                    dp[score][0] > dp[i][0] + 1 or
                    (
                        dp[score][0] == dp[i][0] + 1 and
                        dp[score][1] < dp[i][1] + 1 if k == 1 else dp[i][1]
                    )
                ):
                    dp[score][0] = dp[i][0] + 1
                    dp[score][1] = dp[i][1] + 1 if k == 1 else dp[i][1]

        if i + CENTER_SCORE > target:
            continue

        if (
            dp[i+CENTER_SCORE][0] > dp[i][0] + 1 or
            (
                dp[i+CENTER_SCORE][0] == dp[i][0] + 1 and
                dp[i+CENTER_SCORE][1] < dp[i][1] + 1
            )
        ):
            dp[i+CENTER_SCORE][0] = dp[i][0] + 1
            dp[i+CENTER_SCORE][1] = dp[i][1] + 1

    return dp[-1]


if __name__ == "__main__":
    target = 58
    print(solution(target))
