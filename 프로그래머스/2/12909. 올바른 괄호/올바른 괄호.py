def solution(s):
    stack = []
    for char in s:
        if not stack or char == '(':
            stack.append(char)
            continue

        if char == ')' and stack[-1] == '(':
            stack.pop()

    return bool(not stack)