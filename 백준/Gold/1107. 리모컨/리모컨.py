import sys

input = sys.stdin.readline

def solution(N, M, breaked):
    min_cnt = abs(100 - N)
    for number in range(1_000_001):
        num = str(number)
        for idx in range(len(num)):
            if int(num[idx]) in breaked:
                break
            if idx == len(num) - 1:
                min_cnt = min(min_cnt, abs(int(num) - N) + len(num))
    return min_cnt

N = int(input().rstrip())
M = int(input().rstrip())
breaked = list(map(int, input().split())) if M else []
print(solution(N, M, breaked))
