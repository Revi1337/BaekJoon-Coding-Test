def solution(N, S, nums):
    sm = nums[0]
    left = right = 0
    answer = 1e9
    while left <= right < N:
        if sm >= S:
            answer = min(answer, right - left + 1)
            sm -= nums[left]
            left += 1
        else:
            right += 1
            if right < N:
                sm += nums[right]

    return 0 if answer == 1e9 else answer


N, S = map(int, input().split())
nums = list(map(int, input().split()))
print(solution(N, S, nums))