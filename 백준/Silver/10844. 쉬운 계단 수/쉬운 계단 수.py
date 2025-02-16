def solution(N):
    dp = [[0] * 12 for _ in range(N + 1)]
    dp[1][2:11] = [1] * 9
    for idx in range(2, N + 1):
        for jdx in range(1, 11):
            dp[idx][jdx] = dp[idx - 1][jdx - 1] + dp[idx - 1][jdx + 1]

    return sum(dp[N]) % 1_000_000_000
    
N = int(input().rstrip())
print(solution(N))