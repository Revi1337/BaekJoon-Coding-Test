def solution(N, M, E1, E2):

    def dfs(n):
        if n == v2:
            return
        for nn, nc in tree[n]:
            if check[nn] == -1:
                check[nn] = check[n] + nc
                dfs(nn)

    tree = [[] for _ in range(N + 1)]
    for v1, v2, c in E1:
        tree[v1].append([v2, c])
        tree[v2].append([v1, c])

    ans = []
    for v1, v2 in E2:
        check = [-1] * (N + 1)
        check[v1] = 0
        dfs(v1)
        ans.append(check[v2])

    print(*ans, sep = '\n')


N, M = map(int, input().split())
E1 = [list(map(int, input().split())) for _ in range(N - 1)]
E2 = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, E1, E2)
