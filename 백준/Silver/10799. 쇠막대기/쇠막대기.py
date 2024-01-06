import sys

def solution(data):
    stack = []
    answer = 0
    for idx in range(len(data)):
        if data[idx] == '(':
            stack.append('(')
        else:
            if data[idx - 1] == '(':
                stack.pop()
                answer += len(stack)
            else:
                stack.pop()
                answer += 1
    return answer

data = sys.stdin.readline().rstrip()
print(solution(data))