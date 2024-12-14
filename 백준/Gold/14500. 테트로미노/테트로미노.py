T = [
    # 4
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, -1), (0, -2), (0, -3)],
    [(0, 0), (-1, 0), (-2, 0), (-3, 0)],

    # 2 2
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, -1), (1, 0), (1, -1)],
    [(0, 0), (-1, 0), (0, -1), (-1, -1)],
    [(0, 0), (-1, 0), (0, 1), (-1, 1)],

    # 1 1 2
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],

    # 1, 2, 1
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (1, -1)],

    # 3 1
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)]
]

def solution(N, M, board):
    def rotate_board(board, size):
        r_board = [[0] * size for _ in range(size)]
        for row in range(size):
            for col in range(size):
                r_board[col][size - row - 1] = board[row][col]
        return r_board

    max_length = max(N, M)

    padded_board = [[0] * max_length for _ in range(max_length)]
    for i in range(N):
        for j in range(M):
            padded_board[i][j] = board[i][j]

    boards = [padded_board]
    for _ in range(3):
        boards.append(rotate_board(boards[-1], max_length))

    answer = -1e9
    for row in range(max_length):
        for col in range(max_length):
            for b in boards:
                if b[row][col]:
                    for t in T:
                        sumN = 0
                        for drow, dcol in t:
                            nrow, ncol = row + drow, col + dcol
                            if not (0 <= nrow < max_length and 0 <= ncol < max_length) or b[nrow][ncol] == 0:
                                break
                            sumN += b[nrow][ncol]
                        else:
                            answer = max(answer, sumN)
    return answer

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
