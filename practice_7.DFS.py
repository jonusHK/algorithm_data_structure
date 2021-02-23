# tickets 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미
# 주어진 항공권은 모두 사용해야 함
# 만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return
# 모든 도시를 방문할 수 없는 경우는 주어지지 않음
# 반드시 ICN(인천공항)에서 출발

# 문제의 해결 - 깊이 우선 탐색 (DFS) 응용
# 스택을 이용하여 재귀적인 '한 붓 그리기' 문제를 해결 --> DFS 알고리즘의 응용
# ICN -> [SFO, ATL]
# ATL -> [SFO, ICN]
# SFO -> [ATL]
def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
    return path[::-1]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# 출력값 : ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
    