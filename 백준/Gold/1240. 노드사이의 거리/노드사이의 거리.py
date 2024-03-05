import sys

input = sys.stdin.readline

def solution(n, edges, wish):
    graph = [[] for _ in range(n + 1)]
    for node1, node2, cost in edges:
        graph[node1].append([node2, cost])
        graph[node2].append([node1, cost])

    def dfs(curr_node):
        for next_node, cost in graph[curr_node]:
            if check[next_node] == -1:
                check[next_node] = check[curr_node] + cost
                dfs(next_node)

    for f, t in wish:
        check = [-1] * (n + 1)
        check[f] = 0
        dfs(f)
        print(check[t])

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(n - 1)]
wish = [list(map(int, input().split())) for _ in range(m)]
solution(n, edges, wish)
