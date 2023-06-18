def calc(arr_u, arr_v, sign):
    arr = []
    for u in arr_u:
        for v in arr_v:
            if sign == '+':
                arr.append(u + v)
            elif sign == '-':
                arr.append(u - v)
            else:
                arr.append(u * v)

    return arr


def solution(exp):

    signs = []
    numbers = []

    for s in exp:
        if s in ('*', '+', '-'):
            signs.append(s)
        else:
            numbers.append(int(s))

    n = len(numbers)
    dp = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n):
        dp[1][i].append(numbers[i])

    for i in range(1, n + 1):
        for j in range(n - i + 1):
            for k in range(1, i):
                dp[i][j].extend(calc(dp[k][j], dp[i-k][j+k], signs[j+k-1]))

    return sorted(dp[n][0])


if __name__ == "__main__":
    # 괄호를 자유롭게 넣어 나올 수 있는 모든 결과값을 오름차순으로 정렬하여 반환
    # 수식 길이는 20자를 넘지 않음
    # 수식 연산자 : +, -, *
    # 수식에 들어있는 숫자 : 0 이상 100 미만 정수
    # 연산한 결과는 32비트 정수 범위를 넘지 않음 (2**33 미만)

    exp = "3*2-5*1"
    print(solution(exp))
