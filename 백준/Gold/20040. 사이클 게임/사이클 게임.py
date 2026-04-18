# 2026-04-18
# https://www.acmicpc.net/problem/20040
# 사이클 게임

def solution(N, M, E):

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

    parents = list(range(N))
    for idx, (n1, n2) in enumerate(E):
        if find(n1) == find(n2):
            return idx + 1
        union(n1, n2)

    return 0


N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, E))