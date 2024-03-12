import sys

input = sys.stdin.readline

def solution(integer):
    for number in range(integer):
        digit_sum = number + sum(map(int, str(number)))
        if digit_sum == n:
            return number
    return 0

n = int(input().rstrip())
print(solution(n))