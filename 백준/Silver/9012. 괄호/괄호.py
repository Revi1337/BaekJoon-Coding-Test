def solution(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not len(stack):
                return 'NO'
            stack.pop()
    return 'NO' if len(stack) else 'YES'

loop = int(input())
for _ in range(loop):
    print(solution(input()))