def solution(nums):
    answer = 0
    for integer in nums:
        answer += (integer ** 2)
    print(answer % 10)

solution(list(map(int, input().split())))

