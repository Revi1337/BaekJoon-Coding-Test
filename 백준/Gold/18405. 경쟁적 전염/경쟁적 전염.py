# 2026-03-22
# https://www.acmicpc.net/problem/18405
# bfs

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, K, arr, S, X, Y):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    lst = []
    for row in range(N):
        for col in range(N):
            if arr[row][col]:
                lst.append((arr[row][col], 0, row, col))

    lst.sort()
    queue = deque([*lst])
    while queue:
        sign, time, row, col = queue.popleft()
        if time == S:
            break
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol) and not arr[nrow][ncol]:
                arr[nrow][ncol] = sign
                queue.append((arr[nrow][ncol], time + 1, nrow, ncol))

    return arr[X - 1][Y - 1]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
print(solution(N, K, arr, S, X, Y))
