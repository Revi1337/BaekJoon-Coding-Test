def solution(N, nums):
    """ LCS """
    rnums = nums[::-1]
    dp = [[0] * (N + 1) for _ in range(N + 1)]

    for idx in range(1, N + 1):
        for jdx in range(1, N + 1):
            if nums[idx - 1] == rnums[jdx - 1]:
                dp[idx][jdx] = dp[idx - 1][jdx - 1] + 1
            else:
                dp[idx][jdx] = max(dp[idx - 1][jdx], dp[idx][jdx - 1])

    lcs_length = dp[N][N]
    return N - lcs_length

N = int(input())
nums = list(map(int, input().split()))
print(solution(N, nums))