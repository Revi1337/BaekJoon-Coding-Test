DROW = [-1, 0, 1, 0]
DCOL = [0, 1, 0, -1]

def solution(R, C, T, board):

    inside = lambda row, col: 0 <= row < R and 0 <= col < C
    condi = [row for row in range(R) if board[row][0] == -1]
    urow, ucol = condi[0], 0
    drow, dcol = condi[1], 0

    for _ in range(T):
        # spread
        poss = dict()
        for row in range(R):
            for col in range(C):
                if board[row][col] and board[row][col] != -1:
                    cnt = 0
                    scost = board[row][col] // 5
                    for d in range(4):
                        nrow, ncol = row + DROW[d], col + DCOL[d]
                        if not inside(nrow, ncol) or board[nrow][ncol] == -1:
                            continue
                        cnt += 1
                        poss[(nrow, ncol)] = poss.get((nrow, ncol), 0) + scost
                    poss[(row, col)] = poss.get((row, col), 0) + board[row][col] - scost * cnt
        for (row, col), cnt in poss.items():
            board[row][col] = cnt

        # rotate
        upos = (urow, ucol)
        srow, scol, dir, prev = urow, 1, 1, 0
        while (srow, scol) != upos:
            nrow, ncol = srow + DROW[dir], scol + DCOL[dir]
            if not inside(nrow, ncol):
                dir = (dir - 1) % 4
                continue
            board[srow][scol], prev = prev, board[srow][scol]
            srow, scol = nrow, ncol

        dpos = (drow, dcol)
        srow, scol, dir, prev = drow, 1, 1, 0
        while (srow, scol) != dpos:
            nrow, ncol = srow + DROW[dir], scol + DCOL[dir]
            if not inside(nrow, ncol):
                dir = (dir + 1) % 4
                continue
            board[srow][scol], prev = prev, board[srow][scol]
            srow, scol = nrow, ncol

    board[urow][0] = board[drow][0] = 0
    return sum(sum(line) for line in board)


R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
print(solution(R, C, T, board))
