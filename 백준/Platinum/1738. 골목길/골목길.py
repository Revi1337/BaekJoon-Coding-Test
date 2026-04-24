# 2026-04-24
# https://www.acmicpc.net/problem/1738
# 골목길
# bellman-ford

from collections import deque

def solution(N, M, E):
    INF = -float('inf')
    dist, trace = [INF] * (N + 1), [0] * (N + 1)
    cyc_node = set()

    dist[1] = 0
    for n in range(N):
        for v1, v2, c in E:
            if dist[v1] + c > dist[v2]:
                dist[v2] = dist[v1] + c
                trace[v2] = v1
                if n == N - 1:
                    cyc_node.add(v2)

    if dist[N] == INF:
        print(-1)
        return

    graph = [[] for _ in range(N + 1)]
    for v1, v2, c in E:
        graph[v1].append(v2)

    queue = deque(cyc_node)
    check = [0] * (N + 1)
    for n in cyc_node:
        check[n] = 1

    while queue:
        cn = queue.popleft()
        if cn == N:
            print(-1)
            return
        for nn in graph[cn]:
            if not check[nn]:
                check[nn] = 1
                queue.append(nn)

    ans = []
    while N != trace[N]:
        ans.append(N)
        N = trace[N]

    print(*ans[::-1])

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, E)