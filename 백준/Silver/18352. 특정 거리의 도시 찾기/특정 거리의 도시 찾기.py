import sys
from collections import deque
import heapq

input = sys.stdin.readline

def solution(n, m, k, x, edges):
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in edges:
        graph[v1].append(v2)

    def dijkstra(entrypoint):
        queue = []
        costs = [float('inf')] * (n + 1)
        costs[entrypoint] = 0
        heapq.heappush(queue, [costs[entrypoint], entrypoint])
        while queue:
            cost, road = heapq.heappop(queue)
            if cost > costs[road]:
                continue
            for next_road in graph[road]:
                predicate_cost = cost + 1
                if predicate_cost < costs[next_road]:
                    costs[next_road] = predicate_cost
                    heapq.heappush(queue, [predicate_cost, next_road])
        return costs

    costs = dijkstra(x)

    answer = list(filter(lambda entries: entries[1] == k, enumerate(costs)))
    if not answer:
        print(-1)
    else:
        for idx, _ in sorted(answer):
            print(idx)

n, m, k, x = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
solution(n, m, k, x, edges)

