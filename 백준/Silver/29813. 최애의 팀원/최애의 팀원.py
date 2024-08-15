import sys
from collections import deque

input = sys.stdin.readline

def solution(N, studs):
    queue = deque(studs)
    cache = []
    while len(queue) > 1:
        init, cost = queue.popleft()
        queue.rotate(-(int(cost) - 1))
        ni, nc = queue.popleft()
        cache.append([init, ni])
    return queue[-1][0]

N = int(input())
studs = [input().split() for _ in range(N)]
print(solution(N, studs))
