from collections import deque

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(board):
    st = end = None
    for row in range(16):
        for col in range(16):
            if board[row][col] == 2:
                st = [row, col]
            if board[row][col] == 3:
                end = [row, col]
            if board[row][col] == 1:
                board[row][col] = -1

    board[st[0]][st[1]] = -1
    queue = deque([(st[0], st[1])])

    while queue:
        row, col = queue.popleft()
        if (row, col) == (end[0], end[1]):
            return 1
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if 0 <= nrow < 16 and 0 <= ncol < 16:
                if board[nrow][ncol] != -1:
                    board[nrow][ncol] = -1
                    queue.append((nrow, ncol))

    return 0

T = 10
for _ in range(T):
    seq = int(input())
    board = [list(map(int, input().rstrip())) for _ in range(16)]
    print(f'#{seq} {solution(board)}')