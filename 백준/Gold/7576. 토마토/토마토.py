# 2026-03-13
# https://www.acmicpc.net/problem/7576
# bfs

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(M, N, arr):
    inside = lambda row, col: 0 <= row < N and 0 <= col < M

    queue = deque()
    check = [[0] * M for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if arr[row][col] == 1:
                queue.append([row, col])
                check[row][col] = 1

    ans = 0
    while queue:
        row, col = queue.popleft()
        ans = check[row][col]
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol) and not check[nrow][ncol] and not arr[nrow][ncol]:
                check[nrow][ncol] = check[row][col] + 1
                queue.append([nrow, ncol])

    for row in range(N):
        for col in range(M):
            if not arr[row][col] and not check[row][col]:
                return -1

    return ans - 1

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(solution(M, N, arr))