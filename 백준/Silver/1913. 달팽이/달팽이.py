
import sys

input = sys.stdin.readline

drow = [1, 0, -1, 0]
dcol = [0, 1, 0, -1]

def solution(N, A):
    board = [[0] * N for _ in range(N)]
    target, row, col = N ** 2, 0, 0
    d = 0

    board[row][col] = target
    target -= 1

    while target > 0:
        nrow, ncol = row + drow[d], col + dcol[d]
        if (0 <= nrow < N) and (0 <= ncol < N) and (not board[nrow][ncol]):
            row, col = nrow, ncol
            board[nrow][ncol] = target
            target -= 1
        else:
            d = (d + 1) % 4
    for line in board:
        print(*line)
    for i in range(N):
        for j in range(N):
            if board[i][j] == A:
                print(i + 1, j + 1)
                break

N = int(input())
A = int(input())
solution(N, A)