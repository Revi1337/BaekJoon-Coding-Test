drow = [-1, -1, 0, 1, 1, 1, 0, -1]
dcol = [0, -1, -1, -1, 0, 1, 1, 1]

def solution(board):

    def backtracking(srow, scol, sm, board):
        nonlocal answer
        sm += board[srow][scol][0]
        answer = max(answer, sm)
        board[srow][scol][0] = 0

        for fish in range(1, 17):
            frow = fcol = -1
            for row in range(4):
                for col in range(4):
                    if board[row][col][0] == fish:
                        frow, fcol = row, col
                        break
            if frow == fcol == -1:
                continue

            curr, d = board[frow][fcol]
            for d in range(d, d + 8):
                d = d % 8
                nrow, ncol = frow + drow[d], fcol + dcol[d]
                if not (0 <= nrow < 4 and 0 <= ncol < 4) or (nrow, ncol) == (srow, scol):
                    continue
                board[frow][fcol], board[nrow][ncol] = board[nrow][ncol], [curr, d]
                break

        sd = board[srow][scol][1]
        for offset in range(1, 5):
            nrow = srow + drow[sd] * offset
            ncol = scol + dcol[sd] * offset
            if (0 <= nrow < 4 and 0 <= ncol < 4) and board[nrow][ncol][0] > 0:
                copied = [[[*val] for val in line] for line in board]
                backtracking(nrow, ncol, sm, copied)

    nboard = [[0] * 4 for _ in range(4)]
    for row in range(4):
        for col in range(0, 8, 2):
            nboard[row][col // 2] = board[row][col: col + 2]
            nboard[row][col // 2][1] -= 1
    board = nboard

    answer = 0
    backtracking(0, 0, 0, board)

    return answer

board = [list(map(int, input().split())) for _ in range(4)]
print(solution(board))