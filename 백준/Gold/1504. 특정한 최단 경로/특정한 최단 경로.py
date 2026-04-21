# 2026-04-21
# https://www.acmicpc.net/problem/1504
# 특정한 최단 경로 (좋은 문제인듯?)
# 2차원 dist 가 필요없긴한데.. min() 쪽에서 가독성을 위해 
# dijkstra

import heapq

def solution(N, E, EE, b1, b2):

    INF = float('inf')

    def dijkstra(st):
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

    graph = [[] for _ in range(N + 1)]
    for v1, v2, c in EE:
        graph[v1].append([v2, c])
        graph[v2].append([v1, c])

    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    dijkstra(1)
    dijkstra(b1)
    dijkstra(b2)

    ans = min(
        dist[1][b1] + dist[b1][b2] + dist[b2][N],
        dist[1][b2] + dist[b2][b1] + dist[b1][N]
    )

    return ans if ans != INF else -1

N, E = map(int, input().split())
EE = [list(map(int, input().split())) for _ in range(E)]
b1, b2 = map(int, input().split())
print(solution(N, E, EE, b1, b2))

