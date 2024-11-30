drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, board):

    def count_eat():
        eatable = 0
        for line in board:
            prev, count = line[0], 1
            for idx in range(1, N):
                if line[idx] == prev:
                    count += 1
                else:
                    eatable = max(eatable, count)
                    prev = line[idx]
                    count = 1
            eatable = max(eatable, count)

        for col in range(N):
            prev, count = board[0][col], 1
            for line in board[1:]:
                if line[col] == prev:
                    count += 1
                else:
                    eatable = max(eatable, count)
                    prev = line[col]
                    count = 1
            eatable = max(eatable, count)

        return eatable

    answer = 0
    for row in range(N):
        for col in range(N):
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if 0 <= nrow < N and 0 <= ncol < N and board[row][col] != board[nrow][ncol]:
                    board[row][col], board[nrow][ncol] = board[nrow][ncol], board[row][col]
                    answer = max(answer, count_eat())
                    board[row][col], board[nrow][ncol] = board[nrow][ncol], board[row][col]

    return answer


N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
print(solution(N, board))
