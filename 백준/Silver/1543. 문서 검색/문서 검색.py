import sys

input = sys.stdin.readline

def solution(string: str, target):
    string_length, target_length = len(string), len(target)
    idx = 0
    answer = 0
    while idx < string_length:
        if string[idx: idx + target_length] == target:
            answer += 1
            idx += target_length
        else:
            idx += 1
    return answer


string = input().rstrip()
target = input().rstrip()
print(solution(string, target))
