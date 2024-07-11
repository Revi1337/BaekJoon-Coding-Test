import sys

input = sys.stdin.readline

"""
1. 동점도 생각해야한다.
2. 역전했다가 역전당하는 경우도 생각해야 함.
"""

def solution(N, data):
    prev = [0, 0]
    team1, team2 = [0, 0], [0, 0]
    for goal, time in data:
        h, m = map(int, time.split(':'))
        times = h * 60 + m
        if goal == '1':
            team1[0] += 1
        else:
            team2[0] += 1

        if team1[0] == team2[0]:
            if prev[1] == 1:
                team1[1] += times - prev[0]
            else:
                team2[1] += times - prev[0]
            prev[1] = 0
        elif team1[0] > team2[0]:
            if prev[1] == 0:
                prev[0] = times
                prev[1] = 1
        else:
            if prev[1] == 0:
                prev[0] = times
                prev[1] = 2

    if prev[1] == 1:
        team1[1] += 48 * 60 - prev[0]
    if prev[1] == 2:
        team2[1] += 48 * 60 - prev[0]

    print("%02d:%02d" % (team1[1] // 60, team1[1] % 60))
    print("%02d:%02d" % (team2[1] // 60, team2[1] % 60))


N = int(input())
times = [input().split() for _ in range(N)]
solution(N, times)