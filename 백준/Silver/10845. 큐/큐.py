import sys
from collections import deque

def solution(operations):
    queue = deque()
    for operation in operations:
        if operation[0] == 'front':
            if len(queue):
                print(queue[0])
            else:
                print(-1)
        elif operation[0] == 'back':
            if len(queue):
                print(queue[-1])
            else:
                print(-1)
        elif operation[0] == 'empty':
            if len(queue):
                print(0)
            else:
                print(1)
        elif operation[0] == 'size':
            print(len(queue))
        elif operation[0] == 'pop':
            if len(queue):
                print(queue.popleft())
            else:
                print(-1)
        else:
             queue.append(operation[1])


loop = int(sys.stdin.readline())
operations = [sys.stdin.readline().rstrip().split() for _ in range(loop)]
solution(operations)