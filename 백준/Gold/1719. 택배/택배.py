# 2026-04-23
# https://www.acmicpc.net/problem/1719
# 택배
# V1. floyd-warshall

def solution(N, M, E):
    INF = 1000 * (N + 1)
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    trace = [[0] * (N + 1) for _ in range(N + 1)]

    for v in range(1, N + 1):
        dist[v][v] = 0

    for v1, v2, c in E:
        dist[v1][v2] = dist[v2][v1] = c
        trace[v1][v2] = v2
        trace[v2][v1] = v1

    for mid in range(1, N + 1):
        for st in range(1, N + 1):
            for end in range(1, N + 1):
                if dist[st][mid] + dist[mid][end] < dist[st][end]:
                    dist[st][end] = dist[st][mid] + dist[mid][end]
                    trace[st][end] = trace[st][mid]

    for line in trace[1:]:
        print(*[st if st else '-' for st in line[1:]])


N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, E)
