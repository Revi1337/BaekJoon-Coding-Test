def solution(N, A):
    dp = [float('inf')] * N
    dp[0] = 0
    for idx in range(N):
        for jdx in range(idx + 1, N):
            dp[jdx] = min(dp[jdx], max(dp[idx], (jdx - idx) * (1 + abs(A[idx] - A[jdx]))))

    return dp[N - 1]

N = int(input())
A = list(map(int, input().split()))
print(solution(N, A))
