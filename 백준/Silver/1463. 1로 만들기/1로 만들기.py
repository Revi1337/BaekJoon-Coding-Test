import sys

input = sys.stdin.readline

def solution(N):
    dp = [0] * (N + 1)
    for num in range(2, N + 1):
        dp[num] = dp[num - 1] + 1
        if num % 3 == 0:
            dp[num] = min(dp[num], dp[num // 3] + 1)
        if num % 2 == 0:
            dp[num] = min(dp[num], dp[num // 2] + 1)

    return dp[N]

N = int(input().rstrip())
print(solution(N))
