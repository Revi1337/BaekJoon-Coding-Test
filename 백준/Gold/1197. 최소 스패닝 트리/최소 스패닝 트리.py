import heapq
import sys

input = sys.stdin.readline

def solution(v, e, edges):
    graph = [[] for _ in range(v + 1)]
    for v1, v2, cost in edges:
        graph[v1].append((v2, cost))
        graph[v2].append((v1, cost))

    connect = [-1] * (v + 1)
    queue = []
    heapq.heappush(queue, (0, 1))
    while queue:
        cost, node = heapq.heappop(queue)
        if connect[node] != -1:
            continue
        connect[node] = cost
        for next_node, next_cost in graph[node]:
            if connect[next_node] == -1:
                heapq.heappush(queue, (next_cost, next_node))

    return sum(connect[1:])

v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
print(solution(v, e, edges))
