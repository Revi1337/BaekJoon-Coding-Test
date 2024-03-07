import sys

input = sys.stdin.readline

def solution(n, m, edges):
    node_cnt = n
    INF = float('inf')
    negative_cycle = False

    def bellman_ford(entrypoint):
        distance = [INF] * (node_cnt + 1)
        distance[entrypoint] = 0

        for node in range(node_cnt):
            for curr_node, next_node, edge_cost in edges:
                predicate_cost = distance[curr_node] + edge_cost
                if predicate_cost < distance[next_node] and distance[curr_node] != INF:
                    distance[next_node] = distance[curr_node] + edge_cost
                    if node == node_cnt - 1:
                        nonlocal negative_cycle
                        negative_cycle = True
        return distance

    negative_graph = bellman_ford(1)

    if negative_cycle:
        print("-1")
    else:
        for node in range(2, node_cnt + 1):
            if negative_graph[node] == INF:
                print("-1")
            else:
                print(negative_graph[node])

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
solution(n, m, edges)