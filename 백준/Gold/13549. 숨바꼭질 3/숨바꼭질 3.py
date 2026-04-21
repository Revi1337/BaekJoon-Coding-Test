# 2026-04-21
# https://www.acmicpc.net/problem/13549
# 숨바꼭질 3
# dijkstra

import heapq

def solution(N, K):
    INF = float('inf')
    dist = [INF] * 200_001
    dist[N] = 0
    pq = [[dist[N], N]]

    while pq:
        c, n = heapq.heappop(pq)
        if c > dist[n]:
            continue
        for nn in n - 1, n + 1, n * 2:
            if 0 <= nn <= 200_000:
                if nn == n * 2 and c < dist[nn]:
                    dist[nn] = c
                    heapq.heappush(pq, [dist[nn], nn])
                elif c + 1 < dist[nn]:
                    dist[nn] = c + 1
                    heapq.heappush(pq, [dist[nn], nn])

    return dist[K]

N, K = map(int, input().split())
print(solution(N, K))

