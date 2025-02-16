from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(board):

    inside = lambda row, col : 0 <= row < 12 and 0 <= col < 6

    def breaking(srow, scol):
        check[srow][scol] = 1
        queue.append((srow, scol))
        trace = []

        while queue:
            row, col = queue.popleft()
            trace.append([row, col])
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if inside(nrow, ncol) and board[nrow][ncol] == board[srow][scol] and not check[nrow][ncol]:
                    check[nrow][ncol] = 1
                    queue.append((nrow, ncol))

        return trace

    answer = 0
    queue = deque()
    while True:
        check = [[0] * 6 for _ in range(12)]
        traceable = []
        for row in range(12):
            for col in range(6):
                if board[row][col] != '.' and not check[row][col]:
                    trace = breaking(row, col)
                    if len(trace) >= 4:
                        traceable.append(trace)

        if len(traceable) == 0:
            return answer

        for trace in traceable:
            for row, col in trace:
                board[row][col] = '.'

        for row in range(11, -1, -1):
            for col in range(6):
                if board[row][col] == '.':
                    continue
                srow = row
                for nrow in range(srow + 1, 12):
                    if nrow >= 12 or board[nrow][col] != '.':
                        break
                    srow = nrow
                if row != srow:
                    board[srow][col] = board[row][col]
                    board[row][col] = '.'

        answer += 1


board = [list(input().rstrip()) for _ in range(12)]
print(solution(board))
