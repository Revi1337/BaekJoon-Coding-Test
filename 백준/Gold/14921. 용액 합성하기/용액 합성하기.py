def solution(N, nums):
    left, right = 0, N - 1
    answer = nums[left] + nums[right]
    while left < right:
        tmp = nums[left] + nums[right]
        if abs(answer) > abs(tmp):
            answer = tmp
        if tmp < 0:
            left += 1
        else:
            right -= 1

    return answer

N = int(input())
nums = list(map(int, input().split()))
print(solution(N, nums))