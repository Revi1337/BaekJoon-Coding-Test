def solution(nums: list):
    answer = 0
    for num in nums:
        if num == 1:
            continue
        cnt = 0
        for val in range(2, num + 1):
            if num % val == 0:
                cnt += 1
        if cnt == 1:
            answer += 1
    return answer
_ = input()
print(solution(list(map(int, input().split()))))