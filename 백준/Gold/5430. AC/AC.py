import sys
from collections import deque

input = sys.stdin.readline

def solution(p, n, string):
    string = [] if n == 0 else string[1:-2].split(',')

    queue = deque(string)
    left = n
    reverse = -1
    for operation in p:
        if operation == 'R':
            reverse *= -1
            continue

        if not left:
            return 'error'

        if reverse == 1:
            queue.pop()
        else:
            queue.popleft()
        left -= 1

    if reverse == 1:
        return f'[{",".join(map(str, list(queue)[::-1]))}]'
    else:
        return f'[{",".join(map(str, list(queue)))}]'


t = int(input().rstrip())
for _ in range(t):
    p = input().rstrip()
    n = int(input().rstrip())
    string = input()
    print(solution(p, n, string))