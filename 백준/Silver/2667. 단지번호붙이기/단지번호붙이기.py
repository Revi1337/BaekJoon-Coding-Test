import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, board):

    ansc = 0
    ans = []
    counter = 0

    def dfs(row, col):
        board[row][col] = -1
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < N) and (0 <= ncol < N) and (board[nrow][ncol] == 1):
                nonlocal counter
                counter += 1
                dfs(nrow, ncol)

    for row in range(N):
        for col in range(N):
            if board[row][col] == 1:
                ansc += 1
                counter += 1
                dfs(row, col)
                ans.append(counter)
                counter = 0

    print(ansc)
    print(*sorted(ans), sep = '\n')


N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
solution(N, board)