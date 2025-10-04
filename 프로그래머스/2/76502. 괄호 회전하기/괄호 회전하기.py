from collections import deque

def solution(s):
    string = deque(list(s))
    ans = 0
    for _ in range(len(s)):
        string.rotate(-1)
        stack = []
        for char in string:
            if not stack or char == '[' or char == '(' or char == '{':
                stack.append(char)
                continue

            if char == ']' and stack[-1] == '[':
                stack.pop()
            elif char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()

        if not stack:
            ans += 1

    return ans