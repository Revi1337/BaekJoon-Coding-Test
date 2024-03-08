import sys
import heapq

input = sys.stdin.readline

def solution(n, m, edges,prolog, epilog):
    node_cnt = n
    graph = [[] for _ in range(node_cnt + 1)]
    for v1, v2, cost in edges:
        graph[v1].append([v2, cost])

    def dijkstra(prolog):
        distance = [float('inf') for _ in range(node_cnt + 1)]
        tracking = [float('inf') for _ in range(node_cnt + 1)]
        distance[prolog] = 0
        tracking[prolog] = [prolog]
        queue = []
        heapq.heappush(queue, [distance[prolog], prolog])
        while queue:
            cost, node = heapq.heappop(queue)
            if distance[node] < cost:
                continue
            for next_node, next_cost in graph[node]:
                if cost + next_cost < distance[next_node]:
                    distance[next_node] = cost + next_cost
                    tracking[next_node] = tracking[node] + [next_node]
                    heapq.heappush(queue, [cost + next_cost, next_node])
        return distance, tracking

    costs, paths = dijkstra(prolog)
    print(costs[epilog])
    print(len(paths[epilog]))
    print(" ".join(map(str, paths[epilog])))

n = int(input())
m = int(input())
edges = [list(map(int, input().split())) for _ in range(m)]
prolog, epilog = map(int, input().split())
solution(n, m, edges, prolog, epilog)
