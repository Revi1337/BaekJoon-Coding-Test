import sys

input = sys.stdin.readline

def solution(n):
    answer = 1
    boundary = 1
    while n > boundary:
        boundary += answer * 6
        answer += 1
    return answer
print(solution(int(input().rstrip())))