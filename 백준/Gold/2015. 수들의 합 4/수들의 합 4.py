def solution(N, K, nums):
    sm = ans = 0
    sm_cache = {0: 1} # sum : cnt

    for num in nums:
        sm += num
        if sm - K in sm_cache:
            ans += sm_cache[sm - K]
        sm_cache[sm] = sm_cache.get(sm, 0) + 1

    return ans

N, K = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(N, K, nums))