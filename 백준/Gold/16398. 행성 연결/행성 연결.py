# 2026-04-24
# https://www.acmicpc.net/problem/16398
# 행성 연결
# mst
# V1. kruskal

import heapq

def solution(N, dist):
    conn, pq, ans = [0] * N, [[0, 0]], 0

    while pq:
        cc, cn = heapq.heappop(pq)
        if conn[cn]:
            continue
        conn[cn] = 1
        ans += cc
        for nn, nc in enumerate(dist[cn]):
            if dist[cn][nn] != 0 and not conn[nn]:
                heapq.heappush(pq, [nc, nn])

    return ans

N = int(input())
dist = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, dist))
