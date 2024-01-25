def solution(nums):
    sum = 1
    answer = [0] * 10
    for integer in nums:
        sum *= integer
    for string in str(sum):
        answer[int(string)] += 1
    for integer in answer:
        print(integer)

solution([int(input()) for _ in range(3)])

