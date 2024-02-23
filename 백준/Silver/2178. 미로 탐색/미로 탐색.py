from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(row_cnt, col_cnt, board):
    end_row, end_col = row_cnt - 1, col_cnt - 1

    queue = deque()
    distance = [[0] * col_cnt for _ in range(row_cnt)]

    queue.append((0, 0))
    distance[0][0] = 1
    board[0][0] = 0

    while queue:
        row, col = queue.popleft()
        if row == end_row and col == end_col:
            break
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < row_cnt) and (0 <= ncol < col_cnt) and (board[nrow][ncol]):
                if distance[nrow][ncol] == 0:
                    distance[nrow][ncol] = distance[row][col] + 1
                    board[nrow][ncol] = 0
                    queue.append((nrow, ncol))

    return distance[end_row][end_col]

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
print(solution(n, m, board))
