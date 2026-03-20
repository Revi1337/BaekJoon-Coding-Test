# 2026-03-20
# https://www.acmicpc.net/problem/5427
# bfs

from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(W, H, arr):

    inside = lambda r, c: 0 <= r < H and 0 <= c < W

    ME, EMPTY, FIRE, WALL = '@', '.', '*', '#'

    tcheck = [[-1] * W for _ in range(H)]
    fqueue = deque()
    for row in range(H):
        for col in range(W):
            if arr[row][col] == FIRE:
                fqueue.append((row, col))
                tcheck[row][col] = 0

    while fqueue:
        row, col = fqueue.popleft()
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if inside(nrow, ncol) and arr[nrow][ncol] != WALL and tcheck[nrow][ncol] == -1:
                tcheck[nrow][ncol] = tcheck[row][col] + 1
                fqueue.append((nrow, ncol))

    mqueue = deque()
    check = [[-1] * W for _ in range(H)]
    for row in range(H):
        for col in range(W):
            if arr[row][col] == ME:
                mqueue.append((row, col))
                check[row][col] = 0

    while mqueue:
        row, col = mqueue.popleft()
        if row == 0 or row == H - 1 or col == 0 or col == W - 1:
            return check[row][col] + 1

        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if not inside(nrow, ncol) or arr[nrow][ncol] == WALL or check[nrow][ncol] != -1:
                continue

            ntime = check[row][col] + 1
            if tcheck[nrow][ncol] != -1 and tcheck[nrow][ncol] <= ntime:
                continue

            check[nrow][ncol] = ntime
            mqueue.append((nrow, ncol))

    return 'IMPOSSIBLE'

T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(H)]
    print(solution(W, H, arr))
