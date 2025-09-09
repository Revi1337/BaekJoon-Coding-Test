import sys

input = sys.stdin.readline

def solution(N, K):
    dp = [1_000_001] * (N + 1)
    dp[0] = 0
    for num in range(1, N + 1):
        dp[num] = min(dp[num], dp[num - 1] + 1)
        if num + num // 2 <= N:
            dp[num + num // 2] = min(dp[num + num // 2], dp[num] + 1)

    return 'minigimbob' if dp[N] <= K else 'water'

N, K = map(int, input().rstrip().split())
print(solution(N, K))
