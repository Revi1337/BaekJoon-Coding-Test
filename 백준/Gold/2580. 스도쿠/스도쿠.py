def solution(board):

    def check_three_bound(row, col, num):
        nrow = (row // 3) * 3
        ncol = (col // 3) * 3
        for x in range(3):
            for y in range(3):
                if board[nrow + x][ncol + y] == num:
                    return 1
        return 0

    def backtracking(n):
        nonlocal found
        if found:
            return

        if n == targets_length:
            found = True
            for line in board:
                print(*line)
            return

        cr, cc = targets[n]
        for num in range(1, 10):
            if rows[cr][num] == 0 and cols[cc][num] == 0 and not check_three_bound(cr, cc, num):
                rows[cr][num] = 1
                cols[cc][num] = 1
                board[cr][cc] = num
                backtracking(n + 1)
                board[cr][cc] = 0
                cols[cc][num] = 0
                rows[cr][num] = 0

    targets = []
    rows, cols = [[[0] * 10 for _ in range(9)] for _ in range(2)]
    for row in range(9):
        for col in range(9):
            if board[row][col]:
                rows[row][board[row][col]] = 1
                cols[col][board[row][col]] = 1
            else:
                targets.append([row, col])

    targets_length, found = len(targets), False
    backtracking(0)
    
board = [list(map(int, input().split())) for _ in range(9)]
solution(board)