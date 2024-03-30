import sys

input = sys.stdin.readline

def solution(n):
    numbers = list(range(1, n + 1))
    left = right = 0
    sum_num = numbers[0]
    answer = 0
    while (0 <= left <= right) and (right < n):
        if sum_num == n:
            answer += 1
        if sum_num < n:
            right += 1
            sum_num += numbers[right]
        elif sum_num >= n:
            sum_num -= numbers[left]
            left += 1
    return answer

n = int(input().rstrip())
print(solution(n))