# 2026-04-19
# https://www.acmicpc.net/problem/7511
# 소셜 네트워킹 어플리케이션
# Union-Find

def solution(N, E):

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
    for n1, n2 in E:
        union(n1, n2)

    roots = [find(n) for n in range(N + 1)]

    ans = [1, None]
    for n in range(1, N + 1):
        if roots[n] != roots[ans[0]]:
            ans[1] = n
            break

    print(*ans)

N = int(input())
E = [list(map(int, input().split())) for _ in range(N - 2)]
solution(N, E)