import heapq
import sys

input = sys.stdin.readline

def solution(V, E, edges):
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    for v1, v2, cost in edges:
        graph[v1][v2] = cost
        graph[v2][v1] = cost

    def prim(entrypoint):
        total_cost = 0
        connect = [0] * (V + 1)
        queue = []
        heapq.heappush(queue, (0, entrypoint))
        while queue:
            cost, node = heapq.heappop(queue)
            if connect[node]:
                continue
            connect[node] = 1
            total_cost += cost
            for next_node in range(1, V + 1):
                if graph[node][next_node] != 0 and not connect[next_node]:
                    heapq.heappush(queue, (graph[node][next_node], next_node))
        return total_cost

    return prim(1)

n = int(input().rstrip())
m = int(input().rstrip())
edges = [list(map(int, input().split())) for _ in range(m)]
print(solution(n, m, edges))