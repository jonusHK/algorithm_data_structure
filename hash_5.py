from collections import defaultdict

n, m = map(int, input().split())


team_key_map = defaultdict(list)
member_key_map = {}

for _ in range(n):
    team, cnt = input(), int(input())
    for _ in range(cnt):
        member = input()
        team_key_map[team].append(member)
        member_key_map[member] = team

questions = []
for _ in range(m):
    questions.append((input(), int(input())))

for s, i in questions:
    [print(n, end='\n') for n in sorted(team_key_map[s])] \
        if i == 0 else print(member_key_map[s])
