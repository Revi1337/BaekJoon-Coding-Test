import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(n, m, board):

    cycle = False
    check = [[0] * m for _ in range(n)]

    def dfs(row, col, s_row, s_col, counter):
        nonlocal cycle
        if cycle:
            return
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < n) and (0 <= ncol < m):
                if (counter >= 4) and ((nrow, ncol) == (s_row, s_col)):
                    cycle = True
                    return
                if (not check[nrow][ncol]) and (board[row][col] == board[nrow][ncol]):
                    check[nrow][ncol] = 1
                    dfs(nrow, ncol, s_row, s_col, counter + 1)
                    check[nrow][ncol] = 0

    for row in range(n):
        for col in range(m):
            check[row][col] = 1
            dfs(row, col, row, col, 1)
            check[row][col] = 0
            if cycle:
                 return 'Yes'

    return 'No'

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
print(solution(n, m, board))
