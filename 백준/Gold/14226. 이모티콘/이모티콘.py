# 2026-03-21
# https://www.acmicpc.net/problem/14226
# bfs

from collections import deque

def solution(S):
    check = [[0] * (S + 1) for _ in range(S + 1)]
    check[1][0] = 1
    queue = deque([(1, 0, 0)])  # screen, clipboard, time

    while queue:
        s, c, t = queue.popleft()
        if s == S:
            return t
        if not check[s][s]:
            check[s][s] = 1
            queue.append((s, s, t + 1))
        if c > 0 and s + c <= S and not check[s + c][c]:
            check[s + c][c] = 1
            queue.append((s + c, c, t + 1))
        if s - 1 >= 0 and not check[s - 1][c]:
            check[s - 1][c] = 1
            queue.append((s - 1, c, t + 1))

S = int(input())
print(solution(S))