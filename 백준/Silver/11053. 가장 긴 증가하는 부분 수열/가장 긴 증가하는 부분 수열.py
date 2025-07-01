def solution(A, arr):
    arr, dp = [0] + arr, [0] * (A + 1)

    for idx in range(1, A + 1):
        mx = 0
        for jdx in range(0, idx):
            if arr[jdx] < arr[idx]:
                mx = max(mx, dp[jdx])
        dp[idx] = mx + 1

    return max(dp)

A = int(input())
arr = list(map(int, input().split()))
print(solution(A, arr))
