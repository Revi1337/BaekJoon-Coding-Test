def solution(V, E, edges):
    INF = float('inf')
    graph = [[] for _ in range(V + 1)]
    dist = [[INF] * (V + 1) for _ in range(V + 1)]

    for v1, v2, cost in edges:
        graph[v1].append([v2, cost])
        dist[v1][v2] = cost

    for v in range(1, V + 1):
        dist[v][v] = 0

    for mid in range(1, V + 1):
        for start in range(1, V + 1):
            for end in range(1, V + 1):
                if dist[start][mid] + dist[mid][end] < dist[start][end]:
                    dist[start][end] = dist[start][mid] + dist[mid][end]

    answer = INF
    for start in range(1, V + 1):
        for end in range(1, V + 1):
            if dist[start][end] != 0 and dist[end][start] != 0:
                answer = min(answer, dist[start][end] + dist[end][start])

    return -1 if answer == INF else answer


V, E = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(E)]
print(solution(V, E, edges))