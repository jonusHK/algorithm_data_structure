"""
프로그래머스 - 광물 캐기
"""


def solution(picks, minerals):

    fatigues = [
        [1, 1, 1],
        [5, 1, 1],
        [25, 5, 1]
    ]

    mapper = {
        'diamond': 0,
        'iron': 1,
        'stone': 2
    }

    minerals = minerals[:sum(picks)*5]

    mineral_cnt = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)]
    for i, m in enumerate(minerals):
        mineral_cnt[i//5][mapper[m]] += 1

    mineral_cnt.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    fatigue = 0
    for dia, iron, stone in mineral_cnt:
        for i, p in enumerate(picks):
            if p:
                fatigue += fatigues[i][0] * dia
                fatigue += fatigues[i][1] * iron
                fatigue += fatigues[i][2] * stone
                picks[i] -= 1
                break

    return fatigue


if __name__ == "__main__":
    picks = [1, 3, 2]
    minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

    print(solution(picks, minerals))
