# 2026-04-19
# https://www.acmicpc.net/problem/16562
# 친구비

def solution(N, M, K, A, E):

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
    for n1, n2 in E:
        n1, n2 = n1 - 1, n2 - 1
        union(n1, n2)

    lookup = {}
    for n in range(N):
        root = find(n)
        lookup.setdefault(root, []).append(n)

    cost = 0
    for root in lookup:
        comp = lookup[root]
        cost += min(A[n] for n in comp)

    return cost if cost <= K else 'Oh no'

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, K, A, E))