import sys

input = sys.stdin.readline

"""
1. 3 계단 오르기 x (최대 1개 건너뛰기 가능)
2. 두계단 연속밟기 가능 (3 개 연속 X)
3. 2차원 배열을 통해 dp table 을 초기화
"""
def solution(N, scores):
    scores.insert(0, 0)
    dp = [[0] * 3 for _ in range(N + 1)]
    for idx in range(1, N + 1):
        dp[idx][0] = max(dp[idx - 1][1], dp[idx - 1][2])
        dp[idx][1] = dp[idx - 1][0] + scores[idx]
        dp[idx][2] = dp[idx - 1][1] + scores[idx]

    return max(dp[N][1:])

N = int(input().rstrip())
scores = [int(input().rstrip()) for _ in range(N)]
print(solution(N, scores))
