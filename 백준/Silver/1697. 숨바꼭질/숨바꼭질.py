import sys
from collections import deque

input = sys.stdin.readline

"""
숨바꼭질 (https://www.acmicpc.net/problem/1697)
2024-09-11
"""

def solution(N, K):
    queue = deque([N])
    distance = [-1] * 100_001
    distance[N] = 0
    while queue:
        d = queue.popleft()
        if d == K:
            return distance[d]
        for nd in [d * 2, d + 1, d - 1]:
            if 0 <= nd <= 100_000 and distance[nd] == -1:
                distance[nd] = distance[d] + 1
                queue.append(nd)

N, K = map(int, input().split())
print(solution(N, K))