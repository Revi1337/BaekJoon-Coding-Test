from collections import deque
import sys

input = sys.stdin.readline

def solution(n, operations):
    queue = deque()
    previous = []
    for operation in operations:
        if operation[0] == '3':
            if previous:
                direction = previous.pop()
                if direction == 'left':
                    queue.popleft()
                else:
                    queue.pop()
            continue

        if operation[0] == '1':
            queue.append(operation[1])
            previous.append('right')
        else:
            queue.appendleft(operation[1])
            previous.append('left')

    return "".join(map(str, queue)) if queue else 0


n = int(input().rstrip())
operations = [input().strip().split() for _ in range(n)]
print(solution(n, operations))
