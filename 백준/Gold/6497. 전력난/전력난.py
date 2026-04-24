# 2026-04-24
# https://www.acmicpc.net/problem/6497
# 전력난
# mst
# V1. kruskal

def solution(M, N, E):

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

    E.sort(key=lambda x: x[2])
    parents = list(range(N))
    sm = mst = 0
    for v1, v2, c in E:
        sm += c
        if find(v1) != find(v2):
            union(v1, v2)
            mst += c

    return sm - mst

while True:
    M, N = map(int, input().rstrip().split())
    if M == 0 and N == 0:
        break
    E = [list(map(int, input().rstrip().split())) for _ in range(N)]
    print(solution(M, N, E))