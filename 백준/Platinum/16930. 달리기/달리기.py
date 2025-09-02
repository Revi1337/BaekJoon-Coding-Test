import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, K, arr, srow, scol, erow, ecol):

    EMPTY, WALL = '.', '#'
    inside = lambda row, col : 0 <= row < N and 0 <= col < M

    srow, scol, erow, ecol = srow - 1, scol - 1, erow - 1, ecol - 1
    check = [[-1] * M for _ in range(N)]
    check[srow][scol] = 0
    queue = deque([[srow, scol]])

    while queue:
        row, col = queue.popleft()
        if row == erow and col == ecol:
            return check[row][col]
        for d in range(4):
            for off in range(1, K + 1):
                nrow, ncol = row + drow[d] * off, col + dcol[d] * off
                if not inside(nrow, ncol) or arr[nrow][ncol] == WALL:
                    break
                if check[nrow][ncol] != -1 and check[nrow][ncol] <= check[row][col]:
                    break
                if check[nrow][ncol] == -1:
                    check[nrow][ncol] = check[row][col] + 1
                    queue.append([nrow, ncol])
    return -1

N, M, K = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
srow, scol, erow, ecol = map(int, input().split())
print(solution(N, M, K, arr, srow, scol, erow, ecol))