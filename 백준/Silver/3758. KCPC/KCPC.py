import sys

input = sys.stdin.readline

def solution(n, k, t, m, datas):
    team = {}
    for idx, (i, j, s) in enumerate(datas, start=1):
        meta = {'total': 0, 'last': '0', 'sum': 0, 'score': {ids: 0 for ids in range(1, k + 1)}}
        team[i] = team.get(i, meta)
        if s > team[i]['score'][j]:
            before = team[i]['score'][j]
            team[i]['score'][j] = s
            team[i]['sum'] += (s - before)
        team[i]['total'] += 1
        team[i]['last'] = idx

    sorted_answer = sorted(team, key=lambda tk: (-team[tk]['sum'], team[tk]['total'], team[tk]['last']))
    for idx in range(len(sorted_answer)):
        if sorted_answer[idx] == t:
            return idx + 1

T = int(input())
for _ in range(T):
    n, k, t, m = map(int, input().split())
    datas = [list(map(int, input().split())) for _ in range(m)]
    print(solution(n, k, t, m, datas))

