def solution(string):
    stack = []
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if not len(stack):
                return 'no'
            elif char == ')':
                if stack[-1] != '(':
                    return 'no'
                stack.pop()
            elif char == ']':
                if stack[-1] != '[':
                    return 'no'
                stack.pop()

    return 'yes' if not len(stack) else 'no'

while True:
    string = input()
    if string == '.':
        break
    print(solution(string))