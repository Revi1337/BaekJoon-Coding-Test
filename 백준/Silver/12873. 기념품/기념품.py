import sys
from collections import deque

input = sys.stdin.readline

def solution(N):
    data = deque(range(1, N + 1))
    stage = 1
    while len(data) > 1:
        tstage = stage ** 3
        data.rotate(-(tstage - 1))
        data.popleft()
        stage += 1

    return data[-1]

N = int(input())
print(solution(N))


