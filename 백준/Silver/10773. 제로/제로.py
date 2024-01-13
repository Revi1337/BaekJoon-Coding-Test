def solution(nums):
    stack = []
    for num in nums:
        if num == 0 and len(stack) != 0:
            stack.pop()
        else:
            stack.append(num)
    return sum(stack)

loop = int(input())
nums = [int(input()) for _ in range(loop)]
print(solution(nums))