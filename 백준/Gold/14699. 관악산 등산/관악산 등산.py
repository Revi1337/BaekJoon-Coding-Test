def solution(N, M, H, E):
    H.insert(0, 0)
    adj = [[] for _ in range(N + 1)]
    for v1, v2 in E:
        if H[v1] < H[v2]:
            adj[v1].append(v2)
        else:
            adj[v2].append(v1)

    order = sorted(range(1, N + 1), key=lambda x: -H[x])
    dp = [1] * (N + 1)
    for n in order:
        for nn in adj[n]:
            dp[n] = max(dp[n], 1 + dp[nn])

    print(*dp[1:], sep='\n')

N, M = map(int, input().split())
H = list(map(int, input().split()))
E = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, H, E)
