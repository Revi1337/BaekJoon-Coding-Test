import sys

input = sys.stdin.readline

def solution(strings):
    stack = []
    answer = 0
    for string in strings:
        if string != ']':
            stack.append(string)
            continue

        tmp = 0
        while stack:
            value = stack.pop()
            if value == '[':
                answer += tmp + 8
                break

            length = len(value)
            if value.isdigit():
                tmp += 8
            else:
                tmp += length + 12

    return answer

while True:
    string = input().rstrip()
    if string == '':
        break
    print(solution(string.split()))
