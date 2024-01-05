import sys

loop = int(input())
stack = []
for _ in range(loop):
    operation = sys.stdin.readline().strip()
    if operation.startswith("push"):
        _, integer = operation.split()
        stack.append(integer)
    else:
        if operation == 'pop':
            if not len(stack):
                print(-1)
            else:
                print(stack.pop())
        elif operation == 'size':
            print(len(stack))
        elif operation == 'empty':
            if not len(stack):
                print(1)
            else:
                print(0)
        elif operation == 'top':
            if not len(stack):
                print(-1)
            else:
                print(stack[-1])

