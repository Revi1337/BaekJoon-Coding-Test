# 2026-04-24
# https://www.acmicpc.net/problem/1219
# 오민식의 고민
# bellman-ford

from collections import deque

def solution(N, st, end, M, E, C):
    INF = -float('inf')
    dist = [INF] * N
    dist[st] = C[st]

    cyc = set()
    for n in range(N):
        for v1, v2, c in E:
            if dist[v1] - c + C[v2] > dist[v2]:
                dist[v2] = dist[v1] - c + C[v2]
                if n == N - 1:
                    cyc.add(v2)

    if dist[end] == INF:
        return 'gg'

    if cyc:
        graph = [[] for _ in range(N)]
        for v1, v2, c in E:
            graph[v1].append(v2)
        for n in cyc:
            queue = deque([n])
            check = [0] * N
            check[n] = 1
            while queue:
                n = queue.popleft()
                if n == end:
                    return 'Gee'
                for nn in graph[n]:
                    if not check[nn]:
                        check[nn] = 1
                        queue.append(nn)

    return dist[end]

N, st, end, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
C = list(map(int, input().split()))
print(solution(N, st, end, M, E, C))