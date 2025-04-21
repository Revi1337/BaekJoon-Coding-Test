def solution(N, K, arr):
    for mid in range(N):
        for st in range(N):
            for end in range(N):
                if arr[st][mid] + arr[mid][end] < arr[st][end]:
                    arr[st][end] = arr[st][mid] + arr[mid][end]

    INF = float('inf')
    dp = [[INF] * N for _ in range(1 << N)]
    dp[1 << K][K] = 0

    for v in range(1 << N):
        for c in range(N):
            if dp[v][c] == INF:
                continue

            for n in range(N):
                if v & (1 << n):
                    continue

                new_visited = v | (1 << n)
                new_cost = dp[v][c] + arr[c][n]
                if new_cost < dp[new_visited][n]:
                    dp[new_visited][n] = new_cost

    full_visited = (1 << N) - 1
    answer = min(dp[full_visited])
    return answer

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, K, arr))