import sys

input = sys.stdin.readline

def solution(n, k, numbers):
    answer = sum(numbers[0 : k])
    previous = answer
    left, right = 0, k
    for idx in range(1, n - k + 1):
        temp = previous - numbers[left] + numbers[right]
        previous = temp
        answer = max(answer, temp)
        left += 1
        right += 1

    return answer

n, k = map(int, input().split())
numbers = list(map(int, input().split()))
print(solution(n, k, numbers))
