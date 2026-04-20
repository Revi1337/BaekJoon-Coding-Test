# 2026-04-20
# https://www.acmicpc.net/problem/11085
# 군사 이동
# V2. Kruskal (역방향 Kruskal. 간선이 큰순으로 정렬)

def solution(P, W, start, end, E):

    def find(n):
        while n != parents[n]:
            parents[n] = parents[parents[n]]
            n = parents[n]
        return n

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 < r2:
            parents[r2] = r1
        else:
            parents[r1] = r2

    graph = [[] for _ in range(P)]
    for a, b, w in E:
        graph[a].append([b, w])
        graph[b].append([a, w])

    E.sort(key=lambda x: -x[2])
    parents = list(range(P))
    for n1, n2, cost in E:
        union(n1, n2)
        if find(start) == find(end):
            return cost

    return 0 # Cannot Be Possible

P, W = map(int, input().split())
C, V = map(int, input().split())
E = [tuple(map(int, input().split())) for _ in range(W)]
print(solution(P, W, C, V, E))