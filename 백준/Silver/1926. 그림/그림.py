import sys

sys.setrecursionlimit(10 ** 6)

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(row_length, col_length, board):
    def dfs(row, col):
        nonlocal breath
        breath += 1
        board[row][col] = 0
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < row_length) and (0 <= ncol < col_length) and (board[nrow][ncol]):
                dfs(nrow, ncol)

    counter = 0
    answer = 0
    breath = 0
    for row in range(row_length):
        for col in range(col_length):
            if board[row][col] == 1:
                dfs(row, col)
                counter += 1
                if breath > answer:
                    answer = breath
                breath = 0

    print(counter)
    print(answer)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
solution(n, m, board)