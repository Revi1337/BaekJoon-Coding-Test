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
    answer = -1
    while queue:
        node_cnt = len(queue)
        answer += node_cnt
        for _ in range(node_cnt):
            node = queue.popleft()
            for next_node in graph[node]:
                if check[next_node] == 0:
                    check[next_node] = 1
                    queue.append(next_node)
    return answer


def solution_graph_dfs(n, edges):
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    answer = -1
    check = [0] * (n + 1)
    def DFS(v):
        nonlocal answer
        check[v] = 1
        answer += 1
        for vertext in graph[v]:
            if check[vertext] == 0:
                DFS(vertext)

    DFS(1)
    return answer

n = int(input())
edge_count = int(input())
edges = [list(map(int, input().split())) for _ in range(edge_count)]
print(solution_graph_bfs(n, edges))
print(solution_graph_dfs(n, edges))

