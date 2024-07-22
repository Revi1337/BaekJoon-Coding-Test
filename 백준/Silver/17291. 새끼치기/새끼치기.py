import sys

input = sys.stdin.readline

def solution(N):
    dp = [0] * 21
    dp[0] = dp[1] = 1
    for year in range(2, 21):
        if year % 2 == 0:
            dp[year] = dp[year - 1] * 2 - dp[year - 4] - dp[year - 5]
        else:
            dp[year] = dp[year - 1] * 2

    return dp[N]

N = int(input())
print(solution(N))
