import sys

input = sys.stdin.readline

def solution(N):
    dp = [[1] * 10 for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, 10):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[N][-1] % 10_007

N = int(input().rstrip())
print(solution(N))
