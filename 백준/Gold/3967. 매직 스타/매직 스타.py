def solution(board):

    def validate():
        if sum(ord(board[r][c]) - 64 for r, c in [(0, 4), (1, 3), (2, 2), (3, 1)]) != TARGET:
            return False
        if sum(ord(board[r][c]) - 64 for r, c in [(1, 1), (1, 3), (1, 5), (1, 7)]) != TARGET:
            return False
        if sum(ord(board[r][c]) - 64 for r, c in [(0, 4), (1, 5), (2, 6), (3, 7)]) != TARGET:
            return False
        if sum(ord(board[r][c]) - 64 for r, c in [(3, 1), (3, 3), (3, 5), (3, 7)]) != TARGET:
            return False
        if sum(ord(board[r][c]) - 64 for r, c in [(1, 1), (2, 2), (3, 3), (4, 4)]) != TARGET:
            return False
        if sum(ord(board[r][c]) - 64 for r, c in [(1, 7), (2, 6), (3, 5), (4, 4)]) != TARGET:
            return False
        return True

    def backtracking(n):
        nonlocal found
        if found:
            return

        if n == length:
            if validate():
                found = True
                for line in board:
                    print(*line, sep = '')
            return

        row, col = empties[n]
        curr = board[row][col]
        for alpha in alphas:
            if alpha in left_alphas:
                left_alphas.discard(alpha)
                board[row][col] = alpha
                backtracking(n + 1)
                board[row][col] = curr
                left_alphas.add(alpha)

    left_alphas = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'}
    empties = []
    for row in range(5):
        for col in range(9):
            if board[row][col].isupper():
                left_alphas.discard(board[row][col])
            elif board[row][col] == 'x':
                empties.append((row, col))

    found = False
    length, TARGET = len(empties), 26
    alphas = list(sorted(left_alphas))

    if empties:
        backtracking(0)

board = [list(input().rstrip()) for _ in range(5)]
solution(board)