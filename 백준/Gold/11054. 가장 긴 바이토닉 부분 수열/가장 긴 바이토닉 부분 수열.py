def solution(N, nums):
    inc, dec = [[1] * N for _ in range(2)]

    for idx in range(N): # LIS
        for jdx in range(idx):
            if nums[idx] > nums[jdx] and inc[idx] < inc[jdx] + 1:
                inc[idx] = inc[jdx] + 1

    for idx in range(N - 1, -1, -1): # LDS
        for jdx in range(N - 1, idx, -1):
            if nums[idx] > nums[jdx] and dec[idx] < dec[jdx] + 1:
                dec[idx] = dec[jdx] + 1

    return max(inc[idx] + dec[idx] - 1 for idx in range(N))

N = int(input())
nums = list(map(int, input().split()))
print(solution(N, nums))