def solution(nums: list):
    answer = 0
    for num in nums:
        if num == 1:
            continue
        cnt = 0
        for i in range(2, num):
            if num % i == 0:
                cnt += 1
        if cnt == 0:
            answer += 1
    return answer

_ = input()
print(solution(list(map(int, input().split()))))