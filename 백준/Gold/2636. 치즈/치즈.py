from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(R, C, board):

    total = sum([cost for line in board for cost in line])
    count = 0
    answer = total
    queue = deque()

    while total > 0:

        border = set()
        check = [[0] * C for _ in range(R)]
        check[0][0] = 1
        queue.append((0, 0))
        while queue:
            answer = total
            row, col = queue.popleft()
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if 0 <= nrow < R and 0 <= ncol < C and not check[nrow][ncol]:
                    if board[nrow][ncol] == 0:
                        check[nrow][ncol] = 1
                        queue.append((nrow, ncol))
                    elif board[nrow][ncol] == 1:
                        border.add((nrow, ncol))

        for row, col in border:
            board[row][col] = 0

        count += 1
        total -= len(border)

    print(count, answer, sep = '\n')

R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
solution(R, C, board)
