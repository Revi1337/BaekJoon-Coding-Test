import sys

input = sys.stdin.readline

def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for integer in range(2, n + 1):
        min_value = 1e9
        j = 1
        while (j ** 2) <= integer:
            min_value = min(min_value, dp[integer - (j ** 2)])
            j += 1
        dp[integer] = min_value + 1
    return dp[n]

n = int(input())
print(solution(n))