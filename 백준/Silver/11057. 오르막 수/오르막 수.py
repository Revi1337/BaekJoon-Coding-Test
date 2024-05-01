import sys

input = sys.stdin.readline

def solution(N):
    dp = [[0] * 10 for _ in range(N + 1)]
    dp[0] = [1] * 10
    for i in range(1, N + 1):
        for j in range(10):
            dp[i][j] = sum(dp[i - 1][j:])
    return dp[N][0] % 10_007

N = int(input().rstrip())
print(solution(N))
