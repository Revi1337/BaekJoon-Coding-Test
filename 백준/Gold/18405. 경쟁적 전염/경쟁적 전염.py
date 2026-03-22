# 2026-03-22
# https://www.acmicpc.net/problem/18405
# bfs (queue 기반 bfs 로도 풀 수 있음.)

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, K, arr, S, X, Y):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    lst, check = [], [[-1] * N for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if arr[row][col]:
                check[row][col] = 0
                lst.append((row, col))
    lst.sort(key=lambda pos: arr[pos[0]][pos[1]])

    queue = deque([*lst])
    while queue:
        row, col = queue.popleft()
        if check[row][col] == S:
            break
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol) and not arr[nrow][ncol]:
                check[nrow][ncol] = check[row][col] + 1
                arr[nrow][ncol] = arr[row][col]
                queue.append((nrow, ncol))

    return arr[X - 1][Y - 1]

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
print(solution(N, K, arr, S, X, Y))