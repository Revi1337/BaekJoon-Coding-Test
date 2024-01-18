from collections import deque

def solution(s):
    answer = 0
    brakets = deque(s)
    length = len(s)
    for _ in range(length):
        stack = []
        for braket in brakets:
            if braket in ['(', '[', '{']:
                stack.append(braket)
            else:
                if not stack:
                    stack.append(braket)
                    break
                if braket == ')' and stack[-1] == '(':
                    stack.pop()
                elif braket == ']' and stack[-1] == '[':
                    stack.pop()
                elif braket == '}' and stack[-1] == '{':
                    stack.pop()
        if not stack:
            answer += 1
        brakets.rotate(-1)
    return answer