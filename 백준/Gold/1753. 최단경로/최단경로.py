import sys
import heapq

input = sys.stdin.readline

def solution(V, E, K, edges):
    graph = [[] for _ in range(V + 1)]
    for v1, v2, w in edges:
        graph[v1].append([v2, w])

    costs = [float('inf')] * (V + 1)
    costs[K] = 0
    pq = []
    heapq.heappush(pq, [costs[K], K])
    while pq:
        cost, vertext = heapq.heappop(pq)
        if costs[vertext] < cost:
            continue
        for next_vertext, next_cost in graph[vertext]:
            total_cost = cost + next_cost
            if total_cost < costs[next_vertext]:
                costs[next_vertext] = total_cost
                heapq.heappush(pq, [total_cost, next_vertext])

    for c in costs[1:]:
        if c == float('inf'):
            print('INF')
        else:
            print(c)

V, E = map(int, input().split())
K = int(input())
edges = [list(map(int, input().split())) for _ in range(E)]
solution(V, E, K, edges)