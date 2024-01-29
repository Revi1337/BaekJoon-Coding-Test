def solution_graph_bfs(n, edges):
    from collections import deque
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    queue = deque()
    queue.append(1)
    check = [0] * (n + 1)
    check[1] = 1
    answer = 0
    while queue:
        node_cnt = len(queue)
        answer += node_cnt
        for _ in range(node_cnt):
            node = queue.popleft()
            for next_node in graph[node]:
                if check[next_node] == 0:
                    check[next_node] = 1
                    queue.append(next_node)
    return answer - 1

n = int(input())
edge_count = int(input())
edges = [list(map(int, input().split())) for _ in range(edge_count)]
print(solution_graph_bfs(n, edges))
