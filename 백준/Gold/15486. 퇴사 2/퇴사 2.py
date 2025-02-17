def solution(N, days):
    dp = [0] * (N + 1)
    for idx in range(N - 1, -1, -1):
        if idx + days[idx][0] <= N:
            dp[idx] = max(dp[idx + days[idx][0]] + days[idx][1], dp[idx + 1])
        else:
            dp[idx] = dp[idx + 1]

    return max(dp)

N = int(input())
days = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, days))
