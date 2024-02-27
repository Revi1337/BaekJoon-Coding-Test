import heapq

def solution(vertext_cnt, edges_cnt, entrypoint, edges):
    graph = [[] for _ in range(vertext_cnt + 1)]
    for vertext1, vertext2, cost in edges:
        graph[vertext1].append([vertext2, cost])

    costs = [float('inf') for _ in range(vertext_cnt + 1)]
    costs[entrypoint] = 0

    queue = []
    heapq.heappush(queue, [costs[entrypoint], entrypoint])
    while queue:
        curr_cost, curr_vertext = heapq.heappop(queue)
        if curr_cost < costs[curr_vertext]:
            continue
        for next_vertext, next_cost in graph[curr_vertext]:
            predicate_cost = costs[curr_vertext] + next_cost
            if predicate_cost < costs[next_vertext]:
                costs[next_vertext] = predicate_cost
                heapq.heappush(queue, [predicate_cost, next_vertext])
    for vertext in range(1, vertext_cnt + 1):
        if costs[vertext] == float('inf'):
            print('INF')
        else:
            print(costs[vertext])

v, e = map(int, input().split())
k = int(input())
edges = [list(map(int, input().split())) for _ in range(e)]
solution(v, e, k, edges)