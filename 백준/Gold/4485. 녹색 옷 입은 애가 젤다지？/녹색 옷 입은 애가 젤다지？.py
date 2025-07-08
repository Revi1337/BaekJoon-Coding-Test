drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

from collections import deque

def solution(N, board):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    check = [[-1] * N for _ in range(N)]
    check[0][0] = board[0][0]
    queue = deque([(0, 0)])
    while queue:
        row, col = queue.popleft()
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if not inside(nrow, ncol):
                continue
            if check[nrow][ncol] >= 0:
                if check[row][col] + board[nrow][ncol] < check[nrow][ncol]:
                    check[nrow][ncol] = check[row][col] + board[nrow][ncol]
                    queue.append((nrow, ncol))
            else:
                check[nrow][ncol] = check[row][col] + board[nrow][ncol]
                queue.append((nrow, ncol))

    return check[N - 1][N - 1]

seq = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {seq}: {solution(N, board)}')
    seq += 1

