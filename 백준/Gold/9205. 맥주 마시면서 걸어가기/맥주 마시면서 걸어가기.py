# 2026-03-18
# https://www.acmicpc.net/problem/9205
# bfs

from collections import deque

drow = [-50, 0, 50, 0]
dcol = [0, 50, 0, -50]

def solution(N, H, STO, E):
    check = [0] * N
    queue = deque([(H[0], H[1])])
    while queue:
        row, col = queue.popleft()
        if abs(row - E[0]) + abs(col - E[1]) <= 1000:
            return 'happy'
        for idx in range(N):
            if not check[idx]:
                nrow, ncol = STO[idx]
                if abs(row - nrow) + abs(col - ncol) <= 1000:
                    check[idx] = 1
                    queue.append((nrow, ncol))
    return 'sad'

T = int(input())
for _ in range(T):
    N = int(input())
    H = list(map(int, input().split()))
    STO = [list(map(int, input().split())) for _ in range(N)]
    E = list(map(int, input().split()))
    print(solution(N, H, STO, E))
