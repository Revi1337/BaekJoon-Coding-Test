import sys

input = sys.stdin.readline

def solution(N):
    answer = 0
    for number in range(1, N + 1):
        if number < 10:
            answer += 1
            continue
        string = str(number)
        diff = int(string[1]) - int(string[0])
        for idx in range(1, len(string)):
            if int(string[idx]) - int(string[idx - 1]) != diff:
                break
        else:
            answer += 1
    return answer

N = int(input())
print(solution(N))