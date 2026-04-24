# 2026-04-24
# https://www.acmicpc.net/problem/1922
# 네트워크 연결
# mst
# V1. prim

import heapq
import random

def solution(N, M, E):
    graph = [[] for _ in range(N + 1)]
    for v1, v2, c in E:
        graph[v1].append([v2, c])
        graph[v2].append([v1, c])

    st = random.randint(1, N)
    check = [0] * (N + 1)
    pq = [[0, st]]

    ans = 0
    while pq:
        cc, cn = heapq.heappop(pq)
        if check[cn]:
            continue
        check[cn] = 1
        ans += cc
        for nn, nc in graph[cn]:
            heapq.heappush(pq, [nc, nn])

    return ans

N = int(input().rstrip())
M = int(input().rstrip())
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, E))