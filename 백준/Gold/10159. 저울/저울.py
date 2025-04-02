INF = float('inf')

def solution(N, M, edges):
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    for v1, v2 in edges:
        graph[v1][v2] = 1

    for bridge in range(1, N + 1):
        for v1 in range(1, N + 1):
            for v2 in range(1, N + 1):
                if graph[v1][bridge] + graph[bridge][v2] < graph[v1][v2]:
                    graph[v1][v2] = graph[v1][bridge] + graph[bridge][v2]
    for st in range(1, N + 1):
        cnt = 0
        for end in range(1, N + 1):
            if graph[st][end] == INF and graph[end][st] == INF:
                cnt += 1
        print(cnt - 1)

N = int(input())
M = int(input())
edges = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, edges)