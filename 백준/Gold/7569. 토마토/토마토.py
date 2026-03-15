# 2026-03-15
# https://www.acmicpc.net/problem/7569
# bfs

from collections import deque

dhei = [-1, 1, 0, 0, 0, 0]
drow = [0, 0, -1, 0, 1, 0]
dcol = [0, 0, 0, 1, 0, -1]

def solution(N, M, H, arr):

    inside = lambda hei, row, col: 0 <= hei < H and 0 <= row < N and 0 <= col < M

    queue = deque()
    check = [[[0] * M for _ in range(N)] for _ in range(H)]
    for hei in range(H):
        for row in range(N):
            for col in range(M):
                if arr[hei][row][col] == 1:
                    queue.append([hei, row, col, 0])
                    check[hei][row][col] = 1
                elif arr[hei][row][col] == -1:
                    check[hei][row][col] = -1

    ans = 0
    while queue:
        hei, row, col, cnt = queue.popleft()
        ans = cnt
        for d in range(6):
            nhei, nrow, ncol = hei + dhei[d], row + drow[d], col + dcol[d]
            if inside(nhei, nrow, ncol) and check[nhei][nrow][ncol] == 0 and arr[nhei][nrow][ncol] == 0:
                check[nhei][nrow][ncol] = 1
                queue.append([nhei, nrow, ncol, cnt + 1])

    for hei in range(H):
        for row in range(N):
            for col in range(M):
                if not check[hei][row][col]:
                    return -1
    return ans

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
print(solution(N, M, H, arr))