# 2026-04-21
# https://www.acmicpc.net/problem/4485
# 녹색 옷 입은 애가 젤다지?
# V3. dijkstra

import heapq

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(seq, N, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    INF = float('inf')
    dist = [[INF] * N for _ in range(N)]
    dist[0][0] = arr[0][0]
    pq = [[dist[0][0], 0, 0]]

    while pq:
        cost, row, col = heapq.heappop(pq)
        if cost > dist[row][col]:
            continue
        if row == col == N - 1:
            return f'Problem {seq}: {dist[N - 1][N - 1]}'
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol):
                if cost + arr[nrow][ncol] < dist[nrow][ncol]:
                    dist[nrow][ncol] = cost + arr[nrow][ncol]
                    heapq.heappush(pq, [dist[nrow][ncol], nrow, ncol])

    return None # Impossible

seq = 1
while True:
    N = int(input())
    if not N:
        break
    arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
    print(solution(seq, N, arr))
    seq += 1
