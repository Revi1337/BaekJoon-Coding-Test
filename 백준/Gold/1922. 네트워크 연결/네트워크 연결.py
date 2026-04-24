# 2026-04-24
# https://www.acmicpc.net/problem/1922
# 네트워크 연결
# mst
# V2. kruskal

def solution(N, M, E):

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

    E.sort(key=lambda x: x[2])
    parents = list(range(N + 1))

    ans = 0
    for n1, n2, c in E:
        if find(n1) != find(n2):
            union(n1, n2)
            ans += c

    return ans

N = int(input().rstrip())
M = int(input().rstrip())
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, E))