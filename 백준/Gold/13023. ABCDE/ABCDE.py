# 2026-04-16
# https://www.acmicpc.net/problem/13023
# ABCDE

import sys

sys.setrecursionlimit(10 ** 5)

def solution(N, M, E):

    graph = [[] for _ in range(N)]
    for v1, v2 in E:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(n, depth):
        if depth == 4:
            return 1

        for nn in graph[n]:
            if not check[nn]:
                check[nn] = 1
                if dfs(nn, depth + 1):
                    return 1
                check[nn] = 0
        return 0

    for n in range(N):
        check = [0] * N
        check[n] = 1
        if dfs(n, 0):
            return 1

    return 0

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, E))
