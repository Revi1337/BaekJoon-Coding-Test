import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(M, N, K, positions):
    answer = 0
    board = [[0] * M for _ in range(N)]
    for col, row in positions:
        board[row][col] = 1

    def dfs(row, col):
        board[row][col] = -1
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < N) and (0 <= ncol < M) and (board[nrow][ncol] == 1):
                dfs(nrow, ncol)

    for row in range(N):
        for col in range(M):
            if board[row][col] == 1:
                answer += 1
                dfs(row, col)

    print(answer)


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    positions = [list(map(int, input().split())) for _ in range(K)]
    solution(M, N, K, positions)