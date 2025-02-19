import heapq

INF = float('inf')

def solution(N, M, edges):
    graph = [[] for _ in range(N + 1)]
    for v1, v2, cost in edges:
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])

    costs = [INF] * (N + 1)
    costs[1] = 0
    pq = [[costs[1], 1]]

    while pq:
        cost, ver = heapq.heappop(pq)
        if cost > costs[ver]:
            continue
        for nver, ncost in graph[ver]:
            if cost + ncost < costs[nver]:
                costs[nver] = cost + ncost
                heapq.heappush(pq, [costs[nver], nver])

    return costs[N]

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, edges))