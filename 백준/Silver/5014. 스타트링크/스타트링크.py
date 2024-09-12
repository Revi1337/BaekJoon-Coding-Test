import sys
from collections import deque

input = sys.stdin.readline

"""
스타트링크 (https://www.acmicpc.net/problem/5014)
2024-09-11
"""

def solution(F, S, G, U, D):
    distance = [-1] * (F + 1)
    distance[S] = 0
    queue = deque([S])
    while queue:
        current = queue.popleft()
        if current == G:
            return distance[current]
        for ndir in [current + U, current - D]:
            if (1 <= ndir <= F) and (distance[ndir] == -1):
                queue.append(ndir)
                distance[ndir] = distance[current] + 1

    return 'use the stairs'

F, S, G, U, D = map(int, input().split())
print(solution(F, S, G, U, D))
