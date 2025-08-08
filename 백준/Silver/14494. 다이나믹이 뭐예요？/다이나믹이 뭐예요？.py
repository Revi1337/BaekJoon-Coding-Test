import sys

input = sys.stdin.readline

def solution(N, M):
    dp = [[0] * (M + 1) for _ in range(N + 1)]
    dp[0][0] = 1

    for row in range(1, N + 1):
        for col in range(1, M + 1):
            dp[row][col] = dp[row - 1][col] + dp[row][col - 1] + dp[row - 1][col - 1]

    return dp[N][M] % 1_000_000_007

N, M = map(int, input().split())
print(solution(N, M))
