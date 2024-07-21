import sys
from collections import deque

input = sys.stdin.readline

def solution(N):
    queue = deque(range(1, N + 1))
    trash = []
    while len(queue) > 1:
        trash.append(queue.popleft())
        queue.rotate(-1)

    for t in trash:
        print(t, end = ' ')
    print(queue[0], end = ' ')

N = int(input())
solution(N)
