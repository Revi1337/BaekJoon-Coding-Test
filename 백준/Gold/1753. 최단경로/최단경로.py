# 2026-03-13
# https://www.acmicpc.net/problem/1753
# dijkstra

import heapq

def solution(V, E, st, EE):
    INF = 1e9
    graph = [[] for _ in range(V + 1)]
    for u, v, w in EE:
        graph[u].append([v, w])

    costs = [INF] * (V + 1)
    costs[st] = 0
    pq = [[costs[st], st]]
    while pq:
        c, v = heapq.heappop(pq)
        for nv, nc in graph[v]:
            if c + nc < costs[nv]:
                costs[nv] = c + nc
                heapq.heappush(pq, [costs[nv], nv])

    print(*['INF' if cost == INF else cost for cost in costs[1:]], sep = '\n')

V, E = map(int, input().split())
st = int(input())
EE = [list(map(int, input().split())) for _ in range(E)]
solution(V, E, st, EE)
