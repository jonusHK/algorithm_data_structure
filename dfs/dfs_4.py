"""
프로그래머스 - 여행경로
"""


start = "ICN"
graph = {}
routes = []


def dfs(city):
    while graph[city]:
        dfs(graph[city].pop(0))

    routes.append(city)


def solution(tickets):
    for t in tickets:
        graph.setdefault(t[0], [])
        graph[t[0]].append(t[1])
        graph.setdefault(t[1], [])

    for k in graph.keys():
        graph[k].sort()

    dfs(start)

    return routes[::-1]


if __name__ == '__main__':
    tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    print(solution(tickets))
