def solution(board):

    def check_three_by(row, col, num):
        nc = (col // 3) * 3
        nr = (row // 3) * 3
        for x in range(3):
            for y in range(3):
                if board[nr + x][nc + y] == num:
                    return 1
        return 0

    def backtracking(n):
        nonlocal found
        if found:
            return
        if length == n:
            nonlocal answer
            found = True
            answer = [[*line] for line in board]
            return
        row, col = blank[n]
        for num in range(1, 10):
            if rows[row][num] == cols[col][num] == 0 == check_three_by(row, col, num):
                rows[row][num] = cols[col][num] = 1
                board[row][col] = num
                backtracking(n + 1)
                board[row][col] = 0
                rows[row][num] = cols[col][num] = 0

    rows, cols = [[[0] * 10 for _ in range(9)] for _ in range(2)]
    blank = []
    for row in range(9):
        for col in range(9):
            if board[row][col]:
                rows[row][board[row][col]] = 1
                cols[col][board[row][col]] = 1
            else:
                blank.append((row, col))

    found, answer = False, None
    length = len(blank)
    backtracking(0)

    for line in answer:
        print(*line, sep = '')

board = [list(map(int, input().rstrip())) for _ in range(9)]
solution(board)
