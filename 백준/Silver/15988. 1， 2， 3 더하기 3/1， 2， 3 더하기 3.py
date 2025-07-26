def solution(nums):
    dp = [0] * (1_000_000 + 1)
    dp[1], dp[2], dp[3] = 1, 2, 4

    for idx in range(4, 1_000_000 + 1):
        dp[idx] = (dp[idx - 1] + dp[idx - 2] + dp[idx - 3]) % 1_000_000_009

    print(*[dp[num] for num in nums], sep = '\n')

T = int(input())
nums = [int(input()) for _ in range(T)]
solution(nums)