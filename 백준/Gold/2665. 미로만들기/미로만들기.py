# 2026-03-22
# https://www.acmicpc.net/problem/2665
# 0-1 bfs

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, arr):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    arr[0][0] = -1
    queue = deque([(0, 0, 0)])
    while queue:
        row, col, cnt = queue.popleft()
        if row == N - 1 and col == N - 1:
            return cnt
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol) and arr[nrow][ncol] != -1:
                if arr[nrow][ncol] == 1:
                    queue.appendleft((nrow, ncol, cnt))
                else:
                    queue.append((nrow, ncol, cnt + 1))
                arr[nrow][ncol] = -1

N = int(input())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
print(solution(N, arr))