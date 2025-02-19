def solution(N, edges):
    dp = [[1e9] * (N + 1) for _ in range(N + 1)]
    for mid in range(N + 1):
        dp[mid][mid] = 0

    for v1, v2 in edges:
        dp[v1][v2] = dp[v2][v1] = 1

    for bridge in range(1, N + 1):
        for v1 in range(1, N + 1):
            for v2 in range(1, N + 1):
                if dp[v1][bridge] + dp[bridge][v2] < dp[v1][v2]:
                    dp[v1][v2] = dp[v1][bridge] + dp[bridge][v2]

    costs = [max(line[1:]) for line in dp[1:]]
    mn = min(costs)
    mn_cnt = costs.count(mn)
    candidates = map(lambda x: x[0], filter(lambda x: x[1] == mn, [cost for cost in enumerate(costs, start = 1)]))

    print(mn, mn_cnt)
    print(*candidates)


N = int(input())
edges = []
while True:
    v1, v2 = map(int, input().split())
    if v1 == -1 and v2 == -1:
        break
    edges.append([v1, v2])
solution(N, edges)