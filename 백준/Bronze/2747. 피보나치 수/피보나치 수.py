import sys

input = sys.stdin.readline

def solution(n):
    dp = [0] * 46
    dp[1] = dp[2] = 1
    for num in range(2, n + 1):
        dp[num] = dp[num - 1] + dp[num - 2]
    return dp[n]

n = int(input().rstrip())
print(solution(n))
