import sys

input = sys.stdin.readline

def solution(n, m, numbers):
    answer = 0
    left, right = 0, 1
    while left <= right and right <= n:
        total = sum(numbers[left : right])
        if total < m:
            right += 1
        elif total > m:
            left += 1
        else:
            answer += 1
            right += 1
    return answer

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
print(solution(n, m, numbers))