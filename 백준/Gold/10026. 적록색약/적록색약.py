# 2026-03-15
# https://www.acmicpc.net/problem/10026
# bfs

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    def bfs(arr):
        check = [[0] * N for _ in range(N)]
        cnt = 0
        for srow in range(N):
            for scol in range(N):
                if not check[srow][scol]:
                    cnt += 1
                    init = arr[srow][scol]
                    check[srow][scol] = 1
                    queue = deque([[srow, scol]])
                    while queue:
                        row, col = queue.popleft()
                        for d in range(4):
                            nrow, ncol = row + drow[d], col + dcol[d]
                            if inside(nrow, ncol) and arr[nrow][ncol] == init and not check[nrow][ncol]:
                                check[nrow][ncol] = 1
                                queue.append([nrow, ncol])
        return cnt

    carr = [[''] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if arr[row][col] == 'G':
                carr[row][col] = 'R'
            else:
                carr[row][col] = arr[row][col]

    print(*[bfs(arr), bfs(carr)])

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
solution(N, arr)