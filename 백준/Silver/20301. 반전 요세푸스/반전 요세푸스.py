
import sys
from collections import deque

input = sys.stdin.readline

def solution(N, K, M):
    queue = deque(range(1, N + 1))
    counter = 0
    while queue:
        if counter == M:
            queue.reverse()
            counter = 0
        queue.rotate(-(K - 1))
        print(queue.popleft())
        counter += 1

N, K, M = map(int, input().split())
solution(N, K, M)
