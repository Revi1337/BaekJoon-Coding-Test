import sys
import heapq

input = sys.stdin.readline

def solution(n, e, edges, v1, v2):
    graph = [[] for _ in range(n + 1)]
    for road1, road2, cost in edges:
        graph[road1].append([road2, cost])
        graph[road2].append([road1, cost])

    def dijkstra(entrypoint):
        costs = [float('inf')] * (n + 1)
        costs[entrypoint] = 0
        queue = []
        heapq.heappush(queue, [costs[entrypoint], entrypoint])
        while queue:
            cost, road = heapq.heappop(queue)
            if cost > costs[road]:
                continue
            for next_road, next_cost in graph[road]:
                predicate_cost = cost + next_cost
                if predicate_cost < costs[next_road]:
                    costs[next_road] = predicate_cost
                    heapq.heappush(queue, [predicate_cost, next_road])
        return costs

    entrypoint = dijkstra(1)
    bridge1 = dijkstra(v1)
    bridge2 = dijkstra(v2)

    answer = min(
        entrypoint[v1] + bridge1[v2] + bridge2[n], # 1 --> 2, 2 --> 3, 3 --> 4
        entrypoint[v2] + bridge2[v1] + bridge1[n], # 1 --> 3, 3 --> 2, 2 --> 4
    )

    if answer == float('inf'):
        return -1
    else:
        return answer


n, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
v1, v2 = map(int, input().split())
print(solution(n, e, edges, v1, v2))
