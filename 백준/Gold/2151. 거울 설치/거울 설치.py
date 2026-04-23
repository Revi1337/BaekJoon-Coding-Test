# 2026-04-23
# https://www.acmicpc.net/problem/2151
# 거울 설치
# V1. dijkstra

import heapq

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, arr):

    inside = lambda r, c: 0 <= r < N and 0 <= c < N

    spos = []
    for row in range(N):
        for col in range(N):
            if arr[row][col] == '#':
                spos.append((row, col))
                arr[row][col] = '.'

    (srow, scol), (erow, ecol) = spos
    INF = float('inf')
    dist = [[[INF] * 4 for _ in range(N)] for _ in range(N)]

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

        if arr[nrow][ncol] == '.':
            dist[nrow][ncol][d] = cost
            heapq.heappush(pq, (cost, d, nrow, ncol))
        elif arr[nrow][ncol] == '!':
            if cost < dist[nrow][ncol][d]: # 거울 설치 x
                dist[nrow][ncol][d] = cost
                heapq.heappush(pq, (cost, d, nrow, ncol))
            for nd in [(d + 1) % 4, (d + 3) % 4]: # 거울 설치 o
                if cost + 1 < dist[nrow][ncol][nd]:
                    dist[nrow][ncol][nd] = cost + 1
                    heapq.heappush(pq, (cost + 1, nd, nrow, ncol))

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
print(solution(N, arr))