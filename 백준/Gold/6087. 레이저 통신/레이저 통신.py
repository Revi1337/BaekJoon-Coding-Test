# 2026-04-23
# https://www.acmicpc.net/problem/6087
# 레이저 통신
# V1. dijkstra

import heapq

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(W, H, arr):

    inside = lambda r, c: 0 <= r < H and 0 <= c < W

    spos = []
    for row in range(H):
        for col in range(W):
            if arr[row][col] == 'C':
                spos.append((row, col))
                arr[row][col] = '.'

    (srow, scol), (erow, ecol) = spos
    INF = float('inf')
    dist = [[[INF] * 4 for _ in range(W)] for _ in range(H)]

    pq = []
    for d in range(4):
        dist[srow][scol][d] = 0
        heapq.heappush(pq, (0, d, srow, scol))

    while pq:
        cost, d, row, col = heapq.heappop(pq)
        if cost > dist[row][col][d]:
            continue
        if (row, col) == (erow, ecol):
            return cost

        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol) or arr[nrow][ncol] == '*':
            continue

        if cost < dist[nrow][ncol][d]: # 거울 설치 x
            dist[nrow][ncol][d] = cost
            heapq.heappush(pq, (cost, d, nrow, ncol))

        for nd in [(d + 1) % 4, (d + 3) % 4]: # 거울 설치 o
            if cost + 1 < dist[nrow][ncol][nd]:
                dist[nrow][ncol][nd] = cost + 1
                heapq.heappush(pq, (cost + 1, nd, nrow, ncol))

W, H = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(H)]
print(solution(W, H, arr))