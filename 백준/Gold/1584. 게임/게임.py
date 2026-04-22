# 2026-04-22
# https://www.acmicpc.net/problem/1584
# 게임
# V1. bfs(0-1)

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, arr1, M, arr2):

    inside = lambda row, col: 0 <= row <= 500 and 0 <= col <= 500

    EMPTY, DANGER, DIE = 0, 1, -1

    arr = [[0] * 501 for _ in range(501)]

    for r1, c1, r2, c2 in arr1:
        for row in range(min(r1, r2), max(r1, r2) + 1):
            for col in range(min(c1, c2), max(c1, c2) + 1):
                arr[row][col] = DANGER

    for r1, c1, r2, c2 in arr2:
        for row in range(min(r1, r2), max(r1, r2) + 1):
            for col in range(min(c1, c2), max(c1, c2) + 1):
                arr[row][col] = DIE

    INF = float('inf')
    dist = [[INF] * 501 for _ in range(501)]
    dist[0][0] = 0
    queue = deque([(dist[0][0], 0, 0)])

    while queue:
        cost, row, col = queue.popleft()
        if cost > dist[row][col]:
            continue
        if row == col == 500:
            return dist[500][500]
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if not inside(nrow, ncol) or arr[nrow][ncol] == DIE:
                continue
            if arr[nrow][ncol] == DANGER and cost + 1 < dist[nrow][ncol]:
                dist[nrow][ncol] = cost + 1
                queue.append((dist[nrow][ncol], nrow, ncol))
            elif arr[nrow][ncol] == EMPTY and cost < dist[nrow][ncol]:
                dist[nrow][ncol] = cost
                queue.appendleft((dist[nrow][ncol], nrow, ncol))

    return -1


N = int(input())
arr1 = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
arr2 = [list(map(int, input().split())) for _ in range(M)]
print(solution(N, arr1, M, arr2))
