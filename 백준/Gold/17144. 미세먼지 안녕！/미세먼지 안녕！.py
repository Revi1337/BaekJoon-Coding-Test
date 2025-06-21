# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

# 우 상 좌 하
urow = [0, -1, 0, 1]
ucol = [1, 0, -1, 0]

# 우 하 좌 상
drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

def solution(R, C, T, board):
    conditioner = []
    for row in range(R):
        if board[row][0] == -1:
            conditioner.append((row, 0))

    uur, uuc = conditioner[0]
    ddr, ddc = conditioner[1]

    while T:
        new_board = [[0] * C for _ in range(R)]
        for row in range(R):
            for col in range(C):
                if board[row][col] > 0:
                    curr, count = board[row][col] // 5, 0
                    for d in range(4):
                        nrow, ncol = row + dr[d], col + dc[d]
                        if 0 <= nrow < R and 0 <= ncol < C and board[nrow][ncol] != -1:
                            count += 1
                            new_board[nrow][ncol] += curr
                    new_board[row][col] += board[row][col] - (curr * count)

        d = 0
        prev = 0
        row, col = ddr, 1
        start = (ddr, 0)
        while (row, col) != start:
            nrow, ncol = row + drow[d], col + dcol[d]
            if not (ddr <= nrow < R and 0 <= ncol < C):
                d = (d + 1) % 4
                continue
            new_board[row][col], prev = prev, new_board[row][col]
            row, col = nrow, ncol

        d = 0
        prev = 0
        row, col = uur, 1
        start = (uur, 0)
        while (row, col) != start:
            nrow, ncol = row + urow[d], col + ucol[d]
            if not (0 <= nrow <= uur and 0 <= ncol < C):
                d = (d + 1) % 4
                continue
            new_board[row][col], prev = prev, new_board[row][col]
            row, col = nrow, ncol

        for row, col in conditioner:
            new_board[row][col] = -1

        board = new_board
        T -= 1

    answer = 0
    for row in range(R):
        for col in range(C):
            if board[row][col] != -1:
                answer += board[row][col]

    return answer

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
print(solution(R, C, T, board))