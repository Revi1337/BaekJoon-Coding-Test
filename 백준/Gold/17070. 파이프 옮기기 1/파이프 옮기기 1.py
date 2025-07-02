def solution(N, board):

    def dfs(srow, scol, d):
        if srow == N - 1 and scol == N - 1:
            nonlocal ans
            ans += 1
            return

        if d == 0:
            if scol + 1 < N and not board[srow][scol + 1]:
                dfs(srow, scol + 1, 0)
            if (srow + 1 < N and not board[srow + 1][scol]) and (scol + 1 < N and not board[srow][scol + 1]) and not board[srow + 1][scol + 1]:
                dfs(srow + 1, scol + 1, 2)
        elif d == 1:
            if srow + 1 < N and not board[srow + 1][scol]:
                dfs(srow + 1, scol, 1)
            if (srow + 1 < N and not board[srow + 1][scol]) and (scol + 1 < N and not board[srow][scol + 1]) and not board[srow + 1][scol + 1]:
                dfs(srow + 1, scol + 1, 2)
        elif d == 2:
            if scol + 1 < N and not board[srow][scol + 1]:
                dfs(srow, scol + 1, 0)
            if srow + 1 < N and not board[srow + 1][scol]:
                dfs(srow + 1, scol, 1)
            if (srow + 1 < N and not board[srow + 1][scol]) and (scol + 1 < N and not board[srow][scol + 1]) and not board[srow + 1][scol + 1]:
                dfs(srow + 1, scol + 1, 2)

    ans = 0
    dfs(0, 1, 0)

    return ans

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))