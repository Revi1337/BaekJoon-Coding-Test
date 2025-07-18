def solution(N, M, edges):
    INF = float('inf')
    dp = [[INF] * (N + 1) for _ in range(N + 1)]
    for v in range(1, N + 1):
        dp[v][v] = 0

    for v1, v2 in edges:
        dp[v1][v2] = dp[v2][v1] = 1

    for mid in range(1, N + 1):
        for st in range(1, N + 1):
            for end in range(1, N + 1):
                if dp[st][mid] + dp[mid][end] < dp[st][end]:
                    dp[st][end] = dp[st][mid] + dp[mid][end]

    ans, mn = None, 1e9
    for c1 in range(N, 0, -1):
        for c2 in range(c1 - 1, 0, -1):
            sm = 0
            for v in range(1, N + 1):
                sm += min(dp[v][c1], dp[v][c2]) * 2
            if sm <= mn:
                mn = sm
                ans = [c2, c1]

    print(ans[0], ans[1], mn)

N, M = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(M)]
solution(N, M, edges)