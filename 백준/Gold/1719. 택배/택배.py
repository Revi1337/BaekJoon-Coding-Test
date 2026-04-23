# 2026-04-23
# https://www.acmicpc.net/problem/1719
# 택배
# V2. dijkstra

import heapq

def solution(N, M, E):
    INF = 1000 * (N + 1)

    graph = [[] for _ in range(N + 1)]
    trace = [[0] * (N + 1) for _ in range(N + 1)]
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    for v1, v2, c in E:
        graph[v1].append([v2, c])
        graph[v2].append([v1, c])
        trace[v1][v2] = v2
        trace[v2][v1] = v1

    for st in range(1, N + 1):
        dist[st][st] = 0
        pq = [[dist[st][st], st]]
        while pq:
            c, n = heapq.heappop(pq)
            if c > dist[st][n]:
                continue
            for nn, nc in graph[n]:
                if c + nc < dist[st][nn]:
                    dist[st][nn] = c + nc
                    heapq.heappush(pq, [dist[st][nn], nn])
                    if n == st:
                        trace[st][nn] = nn
                    else:
                        trace[st][nn] = trace[st][n]

    for line in trace[1:]:
        print(*[st if st else '-' for st in line[1:]])

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, E)