import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

def solution(n, nodes):
    graph = [[] for _ in range(n + 1)]
    for (p, c1, c2) in nodes:
        graph[p].append(c1)
        graph[p].append(c2)

    def dfs(node):
        if not mode:
            nonlocal total
            for next_node in graph[node]:
                if next_node != -1 and not check[next_node]:
                    total += 1
                    dfs(next_node)
                    total += 1
        else:
            nonlocal counter
            if graph[node][1] != -1 and not check[graph[node][1]]:
                counter += 1
                dfs(graph[node][1])

    check = [0] * (n + 1)
    mode = 0
    total = 0
    dfs(1)

    check = [0] * (n + 1)
    mode = 1
    counter = 0
    dfs(1)

    return total - counter


n = int(input().rstrip())
nodes = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, nodes))
