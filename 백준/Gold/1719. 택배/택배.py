INF = float('inf')

def solution(N, M, edges):
    dist = [[INF] * (N + 1) for _ in range(N + 1)]
    trace = [[0] * (N + 1) for _ in range(N + 1)]

    for v1, v2, cost in edges:
        if cost < dist[v1][v2]:
            dist[v1][v2] = cost
            dist[v2][v1] = cost
            trace[v1][v2] = v2
            trace[v2][v1] = v1

    for v in range(1, N + 1):
        dist[v][v] = 0

    for mid in range(1, N + 1):
        for st in range(1, N + 1):
            for end in range(1, N + 1):
                if dist[st][mid] + dist[mid][end] < dist[st][end]:
                    dist[st][end] = dist[st][mid] + dist[mid][end]
                    trace[st][end] = trace[st][mid]

    for line in trace[1:]:
        for v in line[1:]:
            print('-' if v == 0 else v, end = ' ')
        print()

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, edges)