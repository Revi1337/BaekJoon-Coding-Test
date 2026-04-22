# 2026-04-22
# https://www.acmicpc.net/problem/14938
# 서강그라운드
# V2. dijkstra

import heapq

def solution(N, M, R, T, E):
    T.insert(0, 0)

    graph = [[] for _ in range(N + 1)]
    for a, b, l in E:
        graph[a].append([b, l])
        graph[b].append([a, l])

    INF = float('inf')
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
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

    ans = 0
    for st in range(1, N + 1):
        sm = 0
        for end in range(1, N + 1):
            if dist[st][end] <= M:
                sm += T[end]
        ans = max(ans, sm)

    return ans

N, M, R = map(int, input().split())
T = list(map(int, input().split()))
E = [list(map(int, input().split())) for _ in range(R)]
print(solution(N, M, R, T, E))