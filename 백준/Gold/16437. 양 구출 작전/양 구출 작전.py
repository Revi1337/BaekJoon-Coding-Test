# 2026-04-26
# https://www.acmicpc.net/problem/16437
# 양 구출 작전
# tree

import sys

sys.setrecursionlimit((10 ** 5) * 2)
input = sys.stdin.readline

def solution(N, E):

    def dfs(n):
        sm = 0
        for nn in tree[n]:
            sm += dfs(nn)

        if signs[n] == 'S':
            amounts[n] += sm
        elif signs[n] == 'W':
            amounts[n] = max(0, sm - amounts[n])

        return amounts[n]

    tree = [[] for _ in range(N + 1)]
    signs, amounts = ['S'] * (N + 1), [0] * (N + 1)
    for n, (s, cnt, pn) in enumerate(E, start=2):
        cnt, pn = int(cnt), int(pn)
        signs[n] = s
        amounts[n] = cnt
        tree[pn].append(n)

    dfs(1)

    return amounts[1]

N = int(input())
E = [input().rstrip().split() for _ in range(N - 1)]
print(solution(N, E))