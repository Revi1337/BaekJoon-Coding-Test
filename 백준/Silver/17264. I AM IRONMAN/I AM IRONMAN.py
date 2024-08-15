import sys

input = sys.stdin.readline

'''
I AM IRONMAN (https://www.acmicpc.net/problem/17264)
2024-08-15
'''

def solution(N, P, W, L, G, pwned, players):

    def update(s = -L):
        nonlocal score
        if score + s < 0:
            score = 0
        else:
            score += s

    pdict = {}
    for player, res in pwned:
        if res == 'L':
            pdict[player] = -L
        else:
            pdict[player] = W

    score = 0
    for player in players:
        if player not in pdict:
            update()
        else:
            update(pdict[player])
        if score >= G:
            return 'I AM NOT IRONMAN!!'

    return 'I AM IRONMAN!!'

N, P = map(int, input().split())
W, L, G = map(int, input().split())
pwned = [input().rstrip().split() for _ in range(P)]
players = [input().rstrip() for _ in range(N)]
print(solution(N, P, W, L, G, pwned, players))
