# 2025-09-01
# https://www.acmicpc.net/problem/16930

import sys
import heapq

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, K, arr, srow, scol, erow, ecol):

    EMPTY, WALL, INF = '.', '#', float('inf')
    inside = lambda row, col : 0 <= row < N and 0 <= col < M

    srow, scol, erow, ecol = srow - 1, scol - 1, erow - 1, ecol - 1
    check = [[INF] * M for _ in range(N)]
    check[srow][scol] = 0
    pq = [(0, srow, scol)]

    while pq:
        time, row, col = heapq.heappop(pq)
        if row == erow and col == ecol:
            return time
        if check[row][col] < time:
            continue
        for d in range(4):
            for off in range(1, K + 1):
                nrow, ncol = row + drow[d] * off, col + dcol[d] * off
                if not inside(nrow, ncol) or arr[nrow][ncol] == WALL:
                    break
                if check[nrow][ncol] <= time:
                    break
                if check[nrow][ncol] == INF:
                    check[nrow][ncol] = time + 1
                    heapq.heappush(pq, (time + 1, nrow, ncol))
    return -1

N, M, K = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
srow, scol, erow, ecol = map(int, input().split())
print(solution(N, M, K, arr, srow, scol, erow, ecol))