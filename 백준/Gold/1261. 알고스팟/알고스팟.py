# 2026-04-21
# https://www.acmicpc.net/problem/1261
# 알고스팟
# V2. dijkstra

import heapq

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    INF = float('inf')
    dist = [[INF] * M for _ in range(N)]
    dist[0][0] = 0
    pq = [[0, 0, 0]]

    while pq:
        cost, row, col = heapq.heappop(pq)
        if cost > dist[row][col]:
            continue
        if row == N - 1 and col == M - 1:
            return dist[row][col]
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol):
                if cost + arr[nrow][ncol] < dist[nrow][ncol]:
                    dist[nrow][ncol] = cost + arr[nrow][ncol]
                    heapq.heappush(pq, [dist[nrow][ncol], nrow, ncol])

    return None # Impossible

M, N = map(int, input().split())
arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]
print(solution(N, M, arr))