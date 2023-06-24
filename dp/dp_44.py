def solution(n, m, arr_m, arr_c):

    dp = [[set()] * (n + 1) for _ in range(n + 1)]
    dp_cost = [int(1e9)] * 1000000001

    for i in range(n + 1):
        dp[i][1].add(arr_c[i])

    for i in range(2, n + 1):
        for j in range(1, n - i + 2):
            _set = set()
            for c1 in dp[1][1]:
                for c2 in dp[2][j-1]:
                    cost = c1 + c2
                    dp_cost[cost] = min(dp_cost[cost], dp_cost[c1] + dp_cost[c2])
                    _set.add(cost)

            for c1 in dp[1][i-1]:
                for c2 in dp[i][1]:
                    cost = c1 + c2
                    dp_cost[cost] = min(dp_cost[cost], dp_cost[c1] + dp_cost[c2])
                    _set.add(cost)

            dp[j][i] = _set

    return dp_cost


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr_m = [0] + list(map(int, input().split()))
    arr_c = [0] + list(map(int, input().split()))
    print(solution(n, m, arr_m, arr_c))
