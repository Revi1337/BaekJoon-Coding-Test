import sys

input = sys.stdin.readline

def solution(n, nums):
    left, right = 0, n - 1
    answer = [nums[left], nums[right]]
    prev = abs(nums[left] + nums[right])
    while left < right:
        sum_num = nums[left] + nums[right]
        if abs(sum_num) < prev:
            prev = abs(sum_num)
            answer = [nums[left], nums[right]]
            if prev == 0:
                break
        if sum_num >= 0:
            right -= 1
        elif sum_num < 0:
            left += 1

    print(answer[0], answer[1])

n = int(input().rstrip())
nums = list(map(int, input().split()))
solution(n, nums)