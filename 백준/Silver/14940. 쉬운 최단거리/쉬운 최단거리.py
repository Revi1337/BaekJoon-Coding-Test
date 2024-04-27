import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(n, m, board):
    target = None
    for row in range(n):
        for col in range(m):
            if board[row][col] == 2:
                target = (row, col)
                break

    check = [[-1] * m for _ in range(n)]
    check[target[0]][target[1]] = 0
    queue = deque([target])
    while queue:
        row, col = queue.popleft()
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < n) and (0 <= ncol < m) and (check[nrow][ncol] == -1):
                if board[nrow][ncol] == 0:
                    check[nrow][ncol] = 0
                elif board[nrow][ncol] == 1:
                    check[nrow][ncol] = check[row][col] + 1
                    queue.append((nrow, ncol))

    for row in range(n):
        for col in range(m):
            if board[row][col] == 0:
                print(0, end = ' ')
            else:
                print(check[row][col], end = ' ')
        print()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
solution(n, m, board)
