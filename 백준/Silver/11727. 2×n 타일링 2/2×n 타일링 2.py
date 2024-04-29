import sys

input = sys.stdin.readline

def solution(n):
    dp = [1] * (n + 1)
    for block in range(2, n + 1):
        dp[block] = dp[block - 1] + dp[block - 2] * 2
    return dp[n] % 10_007

n = int(input().rstrip())
print(solution(n))