import sys
from collections import deque

input = sys.stdin.readline

def solution(N, S, EN, M, E, C):
    INF = -float('inf')
    costs = [INF] * N
    costs[S] = C[S]

    cyc = set()
    for seq in range(N):
        for v1, v2, c in E:
            if costs[v1] - c + C[v2] > costs[v2]:
                costs[v2] = costs[v1] - c + C[v2]
                if seq == N - 1:
                    cyc.add(v2)

    if costs[EN] == INF:
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
                if n == EN:
                    return 'Gee'
                for nn in graph[n]:
                    if not check[nn]:
                        check[nn] = 1
                        queue.append(nn)

    return costs[EN]

N, S, EN, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
C = list(map(int, input().split()))
print(solution(N, S, EN, M, E, C))