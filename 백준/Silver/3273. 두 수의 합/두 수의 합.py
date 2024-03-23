import sys

input = sys.stdin.readline

def solution(n, numbers, x):
    numbers.sort()
    answer = 0
    left, right = 0, n - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == x:
            answer += 1
        if total >= x:
            right -= 1
        elif total <= x:
            left += 1

    return answer

n = int(input().rstrip())
numbers = list(map(int, input().split()))
x = int(input().rstrip())
print(solution(n, numbers, x))
