import sys

input = sys.stdin.readline

def solution(n, integers):
    integers.sort()
    left, right = 0, n - 1
    prev = abs(integers[left] + integers[right])
    answer = [integers[left], integers[right]]

    while left < right:
        score = integers[left] + integers[right]
        if abs(score) < prev:
            prev = abs(score)
            answer = [integers[left], integers[right]]
            if prev == 0:
                break
        if score < 0:
            left += 1
        elif score >= 0:
            right -= 1
    print(answer[0], answer[1])

n = int(input().rstrip())
integers = list(map(int, input().split()))
solution(n, integers)
