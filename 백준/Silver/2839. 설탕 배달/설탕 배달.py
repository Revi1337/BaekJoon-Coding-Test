import sys

input = sys.stdin.readline

def solution(kilogram):
    answer = 0
    while kilogram >= 0:
        if kilogram % 5 == 0:
            answer += int(kilogram // 5)
            return answer
        kilogram -= 3
        answer += 1
    return -1

print(solution(int(input().rstrip())))