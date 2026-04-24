# 2026-04-24
# https://www.acmicpc.net/problem/1197
# 최소 스패닝 트리
# mst
# V2. prim

import heapq
import random

def solution(V, E, EE):
    graph = [[] for _ in range(V + 1)]
    for v1, v2, c in EE:
        graph[v1].append([v2, c])
        graph[v2].append([v1, c])

    st = random.randint(1, V)
    check = [0] * (V + 1)

    ans = 0
    pq = [[0, st, st]]
    while pq:
        c, cn, pn = heapq.heappop(pq)
        if check[cn]:
            continue
        check[cn] = 1
        ans += c
        for nn, nc in graph[cn]:
            if not check[nn]:
                heapq.heappush(pq, [nc, nn, cn])

    return ans

V, E = map(int, input().split())
EE = [list(map(int, input().split())) for _ in range(E)]
print(solution(V, E, EE))
