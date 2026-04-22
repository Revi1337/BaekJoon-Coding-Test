# 2026-04-22
# https://www.acmicpc.net/problem/5972
# 택배 배송

import heapq

def solution(N, M, E):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in E:
        graph[a].append([b, c])
        graph[b].append([a, c])

    INF = float('inf')
    dist = [INF] * (N + 1)
    dist[1] = 0
    pq = [[dist[1], 1]]

    while pq:
        c, n = heapq.heappop(pq)
        if c > dist[n]:
            continue
        if n == N:
            return dist[n]
        for nn, nc in graph[n]:
            if c + nc < dist[nn]:
                dist[nn] = c + nc
                heapq.heappush(pq, [dist[nn], nn])


N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, E))
