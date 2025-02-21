import heapq

INF = 1e9

def solution(N, M, edges, S, T):
    graph = [[] for _ in range(N + 1)]
    for v1, v2, cost in edges:
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])

    costs = [INF] * (N + 1)
    costs[S] = 0
    pq = [[costs[S], S]]

    while pq:
        cc, cn = heapq.heappop(pq)
        if cc > costs[cn]:
            continue
        for nn, nc in graph[cn]:
            if cc + nc < costs[nn]:
                costs[nn] = cc + nc
                heapq.heappush(pq, [costs[nn], nn])

    return costs[T]


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
S, T = map(int, input().split())
print(solution(N, M, edges, S, T))

