import sys

input = sys.stdin.readline

def solution(n, m, numbers):
    numbers.sort()
    left, right = 0, n - 1
    answer = 0
    while left < right:
        sum_num = numbers[left] + numbers[right]
        if sum_num == m:
            answer += 1
        if sum_num >= m:
            right -= 1
        elif sum_num <= m:
            left += 1
    return answer

n = int(input().rstrip())
m = int(input().rstrip())
numbers = list(map(int, input().split()))
print(solution(n, m, numbers))