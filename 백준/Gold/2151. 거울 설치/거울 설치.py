import sys
from collections import deque

input = sys.stdin.readline

# 상 우 하 좌
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, arr):

    DOOR, MIR, WALL, EMPTY = '#', '!', '*', '.'
    inside = lambda row, col : 0 <= row < N and 0 <= col < N

    doors = []
    for row in range(N):
        for col in range(N):
            if arr[row][col] == DOOR:
                doors.append([row, col])

    INF = 1e9
    check = [[[INF] * N for _ in range(N)] for _ in range(4)]

    queue = deque()
    row, col = doors[0]
    for d in range(4):
        check[d][row][col] = 0
        queue.append([row, col, d])

    while queue:
        row, col, d = queue.popleft()
        if [row, col] == doors[1]:
            return check[d][row][col]

        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol) or arr[nrow][ncol] == WALL:
            continue
        if check[d][nrow][ncol] > check[d][row][col]:
            check[d][nrow][ncol] = check[d][row][col]
            queue.appendleft([nrow, ncol, d])
        if arr[nrow][ncol] == MIR:
            for nd in [(d + 1) % 4, (d + 3) % 4]:
                if check[nd][nrow][ncol] > check[d][row][col] + 1:
                    check[nd][nrow][ncol] = check[d][row][col] + 1
                    queue.append([nrow, ncol, nd])

N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
print(solution(N, arr))
