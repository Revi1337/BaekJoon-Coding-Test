drow = [0, 1, 1]
dcol = [1, 1, 0]

def solution(M, N, board):

    inside = lambda row, col: 0 <= row < M and 0 <= col < N

    board = [list(line) for line in board]
    ans = 0
    while True:
        rem = set()
        for row in range(M):
            for col in range(N):
                if board[row][col] == '':
                    continue
                sign, tmp = board[row][col], {(row, col)}
                for d in range(3):
                    nrow, ncol = row + drow[d], col + dcol[d]
                    if inside(nrow, ncol) and board[nrow][ncol] == sign:
                        tmp.add((nrow, ncol))
                if len(tmp) == 4:
                    rem |= tmp

        if not rem:
            return ans

        for row, col in rem:
            board[row][col] = ''
            ans += 1

        for col in range(N):
            for row in range(M - 1, -1, -1):
                if board[row][col] != '':
                    while True:
                        nrow, ncol = row + 1, col
                        if inside(nrow, ncol) and board[nrow][ncol] == '':
                            board[row][col], board[nrow][ncol] = board[nrow][ncol], board[row][col]
                            row, col = nrow, ncol
                        else:
                            break
