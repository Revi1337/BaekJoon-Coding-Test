import sys
from collections import deque

input = sys.stdin.readline

"""
맥주 마시면서 걸어가기 (https://www.acmicpc.net/problem/9205)
2024-09-13
"""

drow = [-50, 0, 50, 0]
dcol = [0, 50, 0, -50]

def solution(N, home, marks, fes):
    check = [0] * N
    queue = deque([(home[0], home[1])])
    while queue:
        row, col = queue.popleft()
        if abs(row - fes[0]) + abs(col - fes[1]) <= 1000:
            return 'happy'
        for idx in range(N):
            if not check[idx]:
                nrow, ncol = marks[idx]
                if abs(row - nrow) + abs(col - ncol) <= 1000:
                    check[idx] = 1
                    queue.append((nrow, ncol))
    return 'sad'

T = int(input())
for _ in range(T):
    N = int(input())
    home = list(map(int, input().split()))
    marks = [list(map(int, input().split())) for _ in range(N)]
    fes = list(map(int, input().split()))
    print(solution(N, home, marks, fes))