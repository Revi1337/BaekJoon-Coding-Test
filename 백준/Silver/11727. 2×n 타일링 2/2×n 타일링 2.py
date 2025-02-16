def solution(N):
    dp = [1] * (N + 1)
    for idx in range(2, N + 1):
        dp[idx] = dp[idx - 1] + dp[idx - 2] * 2

    return dp[N] % 10007

N = int(input())
print(solution(N))