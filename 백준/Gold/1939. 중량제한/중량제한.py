import heapq

"""
다익스트라를 최대힙으로
"""
def solution(N, M, bridges, start, end):
    graph = [[] for _ in range(N + 1)]
    for a, b, c in bridges:
        graph[a].append((b, c))
        graph[b].append((a, c))

    pq = [(-1_000_000_000, start)]
    visited = [False] * (N + 1)
    while pq:
        weight, node = heapq.heappop(pq)
        weight = -weight
        if node == end:
            return weight
        if visited[node]:
            continue
        visited[node] = True
        for next_node, limit in graph[node]:
            if not visited[next_node]:
                heapq.heappush(pq, (-min(weight, limit), next_node))

    return 0

N, M = map(int, input().split())
bridges = [list(map(int, input().split())) for _ in range(M)]
start, end = map(int, input().split())
print(solution(N, M, bridges, start, end))