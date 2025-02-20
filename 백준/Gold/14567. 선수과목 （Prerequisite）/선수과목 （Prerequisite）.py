INF = float('inf')

def solution(N, M, edges):
    graph = [[] for _ in range(N + 1)]
    counter = [0] * (N + 1)
    for v1, v2 in edges:
        graph[v1].append(v2)
        counter[v2] += 1

    answer = [INF] * (N + 1)
    for idx in range(1, N + 1):
        if counter[idx] == 0:
            answer[idx] = 1

    for curr in range(1, N + 1):
        for next in graph[curr]:
            if answer[next] != INF:
                answer[next] = max(answer[next], answer[curr] + 1)
            else:
                answer[next] = min(answer[next], answer[curr] + 1)

    print(*answer[1:])


N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, edges)
