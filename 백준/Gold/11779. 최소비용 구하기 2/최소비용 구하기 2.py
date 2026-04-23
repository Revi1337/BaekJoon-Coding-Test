# 2026-04-23
# https://www.acmicpc.net/problem/11779
# 최소비용 구하기 2
# dijkstra

import heapq

def solution(N, M, E, st, end):
    INF = float('inf')

    graph = [[] for _ in range(N + 1)]
    for v1, v2, c in E:
        graph[v1].append([v2, c])

    dist = [INF] * (N + 1)
    dist[st] = 0
    pq = [[dist[st], st]]

    trace = [[] for _ in range(N + 1)]
    for n in range(1, N + 1):
        trace[n].append(n)

    while pq:
        c, n = heapq.heappop(pq)
        if c > dist[n]:
            continue
        if n == end:
            print(dist[end])
            print(len(trace[end]))
            print(*trace[end])
            return
        for nn, nc in graph[n]:
            if c + nc < dist[nn]:
                dist[nn] = c + nc
                heapq.heappush(pq, [dist[nn], nn])
                trace[nn] = trace[n] + [nn]

N = int(input())
M = int(input())
E = [list(map(int, input().split())) for _ in range(M)]
st, end = map(int, input().split())
solution(N, M, E, st, end)
