import sys

open = sys.stdin.readline

drow = [1, 1, 1]
dcol = [-1, 0, 1]

def solution(N, M, board):
    col_length = len(board[0])
    answer = 1e9

    def dfs(row, col, dir, total):
        if row == N - 1:
            nonlocal answer
            answer = min(answer, total)
            return
        for d in range(3):
            if d != dir and dir is not None:
                nrow, ncol = row + drow[d], col + dcol[d]
                if (0 <= nrow < N) and (0 <= ncol < M) and (check[nrow][ncol] == 0):
                    check[nrow][ncol] = 1
                    dfs(nrow, ncol, d, total + board[nrow][ncol])
                    check[nrow][ncol] = 0

    for col in range(col_length):
        check = [[0] * M for _ in range(N)]
        check[0][col] = 1
        dfs(0, col, -1, board[0][col])
        check[0][col] = 0

    return answer

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
