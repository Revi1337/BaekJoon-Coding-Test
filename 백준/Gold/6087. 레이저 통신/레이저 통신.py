import sys
from collections import deque

input = sys.stdin.readline

# 상 우 하 좌
drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(W, H, arr):

    WALL, EMPTY, TAR = '*', '.', 'C'
    inside = lambda row, col : 0 <= row < H and 0 <= col < W

    tars = []
    for row in range(H):
        for col in range(W):
            if arr[row][col] == TAR:
                tars.append([row, col])

    INF = 1e9
    check = [[[INF] * W for _ in range(H)] for _ in range(4)]

    queue = deque()
    row, col = tars[0]
    for d in range(4):
        check[d][row][col] = 0
        queue.append([row, col, d])

    while queue:
        row, col, d = queue.popleft()
        if [row, col] == tars[1]:
            return check[d][row][col]

        nrow, ncol = row + drow[d], col + dcol[d]
        if not inside(nrow, ncol) or arr[nrow][ncol] == WALL:
            continue

        if check[d][nrow][ncol] > check[d][row][col]:
            check[d][nrow][ncol] = check[d][row][col]
            queue.appendleft([nrow, ncol, d])
        for nd in (d + 1) % 4, (d + 3) % 4:
            if check[nd][nrow][ncol] > check[d][row][col] + 1:
                check[nd][nrow][ncol] = check[d][row][col] + 1
                queue.append([nrow, ncol, nd])

W, H = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(H)]
print(solution(W, H, arr))