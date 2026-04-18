# 2026-04-18
# https://www.acmicpc.net/problem/1976
# 여행 가자
# Union-Find

def solution(N, M, E, T):

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

    parents = list(range(N + 1))
    for n1 in range(N):
        for n2, con in enumerate(E[n1]):
            if con:
                union(n1, n2)

    ans = [find(n - 1) for n in T]
    for an in ans:
        if an != ans[0]:
            return 'NO'
    return 'YES'

N = int(input())
M = int(input())
E = [list(map(int, input().split())) for _ in range(N)]
T = list(map(int, input().split()))
print(solution(N, M, E, T))
