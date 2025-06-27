def solution(N, M, K, roads, holes):
    edges = []
    for v, nv, c in roads:
        edges.append([v, nv, c])
        edges.append([nv, v, c])
    for v, nv, c in holes:
        edges.append([v, nv, -c])

    dist = [1e9] * (N + 1)
    dist[0] = 0
    for _ in range(N):
        for v, nv, cost in edges:
            if dist[nv] > dist[v] + cost:
                dist[nv] = dist[v] + cost
                if _ == N - 1:
                    return 'YES'

    return 'NO'

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    holes = [list(map(int, input().split())) for _ in range(K)]
    print(solution(N, M, K, roads, holes))