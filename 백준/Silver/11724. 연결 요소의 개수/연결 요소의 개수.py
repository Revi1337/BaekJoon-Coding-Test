import sys

input = sys.stdin.readline

def solution(N, M, edges):
    graph = [[] for _ in range(N + 1)]
    check = [0] * (N + 1)
    answer = 0
    for v1, v2 in edges:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(entry):
        check[entry] = 1
        for nv in graph[entry]:
            if not check[nv]:
                dfs(nv)

    for v in range(1, N + 1):
        if not check[v]:
            answer += 1
            dfs(v)

    return answer

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, edges))