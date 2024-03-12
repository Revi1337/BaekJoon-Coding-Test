import sys

input = sys.stdin.readline

def solution(a, b, v):
    answer = (v - b) / (a - b)
    if answer == int(answer):
        return int(answer)
    return int(answer) + 1

a, b, v = map(int, input().split())
print(solution(a, b, v))