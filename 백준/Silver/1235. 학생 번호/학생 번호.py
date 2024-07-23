import sys

input = sys.stdin.readline

def solution(N, nums):
    answer = float('inf')
    length = len(nums[0])
    for idx in range(length):
        new = list(map(lambda x: x[idx:], nums))
        for val in new:
            cnt = new.count(val)
            if cnt >= 2:
                break
        else:
            answer = min(answer, len(new[0]))
    return answer

N = int(input())
nums = [input().strip() for _ in range(N)]
print(solution(N, nums))
