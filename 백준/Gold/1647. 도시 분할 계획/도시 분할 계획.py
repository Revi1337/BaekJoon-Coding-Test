# 2026-04-24
# https://www.acmicpc.net/problem/1647
# 도시 분할 계획
# mst
# V2. prim

import heapq
import random

def solution(N, M, E):
    graph = [[] for _ in range(N + 1)]
    for v1, v2, c in E:
        graph[v1].append([v2, c])
        graph[v2].append([v1, c])

    INF = float('inf')
    dist, check = [INF] * (N + 1), [0] * (N + 1)

    st = random.randint(1, N)
    dist[st] = 0

    ans = mx = 0
    pq = [[0, st]]
    while pq:
        cc, cn = heapq.heappop(pq)
        if check[cn]:
            continue

        check[cn] = 1
        ans += cc
        mx = max(mx, cc)

        for nn, nc in graph[cn]:
            if not check[nn] and nc < dist[nn]:
                dist[nn] = nc
                heapq.heappush(pq, [nc, nn])

    return ans - mx

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, E))
