def solution(N, M, R, T, edges):

    def dfs(v, dist, dists):
        for nv, l in graph[v]:
            new_dist = dist + l
            if new_dist <= M and new_dist < dists[nv]:
                dists[nv] = new_dist
                dfs(nv, new_dist, dists)

    T.insert(0, 0)
    graph = [[] for _ in range(N + 1)]
    for v1, v2, l in edges:
        graph[v1].append((v2, l))
        graph[v2].append((v1, l))

    answer = 0
    for start in range(1, N + 1):
        dists = [float('inf')] * (N + 1)
        dists[start] = 0
        dfs(start, 0, dists)
        total = sum(T[i] for i in range(1, N + 1) if dists[i] <= M)
        answer = max(answer, total)

    return answer

N, M, R = map(int, input().split())
T = list(map(int, input().split())) # N
edges = [list(map(int, input().split())) for _ in range(R)]
print(solution(N, M, R, T, edges))