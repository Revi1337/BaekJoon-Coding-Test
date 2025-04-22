def solution(N, edges, A, B):

    graph = [[] for _ in range(N + 1)]
    for v1, v2 in edges:
        graph[v2].append(v1)

    check = [0] * (N + 1)
    for node in A, B:
        if not check[node]:
            check[node] = 1
        else:
            return node

        while True:
            if graph[node]:
                node = graph[node][0]
                if not check[node]:
                    check[node] = 1
                else:
                    return node
            else:
                break

T = int(input())
for _ in range(T):
    N = int(input())
    edges = [list(map(int, input().split())) for _ in range(N - 1)]
    A, B = map(int, input().split())
    print(solution(N, edges, A, B))