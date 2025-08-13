def solution(N):
    MOD = 1_000_000_000
    dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]

    for d in range(1, 10):
        dp[1][d][1 << d] = 1

    for length in range(2, N + 1):
        for last in range(10):
            for mask in range(1 << 10):
                if dp[length - 1][last][mask] == 0:
                    continue
                for next in [last - 1, last + 1]:
                    if 0 <= next <= 9:
                        next_mask = mask | (1 << next)
                        dp[length][next][next_mask] = (dp[length][next][next_mask] + dp[length - 1][last][mask]) % MOD

    return sum(dp[N][d][(1 << 10) - 1] for d in range(10)) % MOD

N = int(input())
print(solution(N))