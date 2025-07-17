def solution(N, M, E):

    def find(n):
        if n == parents[n]:
            return n

        parents[n] = find(parents[n])
        return parents[n]

    def union(n1, n2):
        r1, r2 = find(n1), find(n2)
        if r1 < r2:
            parents[r2] = r1
        else:
            parents[r1] = r2

    E.sort(key=lambda x: x[2])
    parents = list(range(N + 1))

    ans, mx = 0, 1
    for v1, v2, cost in E:
        if find(v1) != find(v2):
            ans += cost
            mx = max(mx, cost)
            union(v1, v2)

    return ans - mx

N, M = map(int, input().split())
E = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, M, E))