def solution(N, K, arr):
    ar2 = [lst[1:] for lst in arr]
    ar2.sort(key = lambda x: (-x[0], -x[1], -x[2]))

    dp = [0] * N
    dp[0] = 1
    for idx in range(1, N):
        if ar2[idx] == ar2[idx - 1]:
            dp[idx] = dp[idx - 1]
        else:
            dp[idx] = idx + 1

    return dp[K - 1]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, K, arr))