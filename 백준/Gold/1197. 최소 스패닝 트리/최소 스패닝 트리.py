# 2026-04-24
# https://www.acmicpc.net/problem/1197
# 최소 스패닝 트리
# mst
# V1. Kruskal

def solution(V, E, EE):

    def find(n):
        while n != parents[n]:
            parents[n] = parents[parents[n]]
            n = parents[n]
        return n

    def union(n1, n2):
        r1, r2 = find(n1), find(n2),
        if r1 < r2:
            parents[r2] = r1
        else:
            parents[r1] = r2

    EE.sort(key=lambda x: x[2])
    parents = list(range(V + 1))
    ans = 0
    for n1, n2, c in EE:
        if find(n1) != find(n2):
            union(n1, n2)
            ans += c

    return ans

V, E = map(int, input().split())
EE = [list(map(int, input().split())) for _ in range(E)]
print(solution(V, E, EE))
