# 2026-04-27
# https://www.acmicpc.net/problem/2533
# 사회망 서비스 (SNS)
# tree
# dfs(Stack 기반) + dp

import sys

input = sys.stdin.readline

def solution(N, E):
    graph = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        graph[v1].append(v2)
        graph[v2].append(v1)

    dp = [[0, 1] for _ in range(N + 1)]
    parent = [0] * (N + 1)
    stack = [1]
    order = []

    parent[1] = -1
    while stack:
        n = stack.pop()
        order.append(n)
        for nn in graph[n]:
            if nn != parent[n]:
                parent[nn] = n
                stack.append(nn)

    for n in order[::-1]:
        for nn in graph[n]:
            if nn != parent[n]:
                dp[n][0] += dp[nn][1]
                dp[n][1] += min(dp[nn][0], dp[nn][1])

    return min(dp[1][0], dp[1][1])


N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 1)]
print(solution(N, E))