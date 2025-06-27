def solution(N, M, K, roads, holes):
    graph = [[] for _ in range(N + 1)]
    for v1, v2, cost in roads:
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])
    for v1, v2, cost in holes:
        graph[v1].append([v2, -cost])

    def has_negative_cycle():
        dist = [1e9] * (N + 1)
        dist[0] = 0
        for _ in range(N):
            for cur in range(1, N + 1):
                for nxt, cost in graph[cur]:
                    if dist[nxt] > dist[cur] + cost:
                        dist[nxt] = dist[cur] + cost
                        if _ == N - 1:
                            return True
        return False

    return 'YES' if has_negative_cycle() else 'NO'

T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(M)]
    holes = [list(map(int, input().split())) for _ in range(K)]
    print(solution(N, M, K, roads, holes))