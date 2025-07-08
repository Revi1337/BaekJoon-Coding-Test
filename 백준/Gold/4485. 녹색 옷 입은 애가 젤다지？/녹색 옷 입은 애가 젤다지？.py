drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

import heapq

def solution(N, board):

    inside = lambda row, col: 0 <= row < N and 0 <= col < N

    pq = [(board[0][0], 0, 0)]
    board[0][0] = -1
    while pq:
        cost, row, col = heapq.heappop(pq)
        if row == N - 1 and col == N - 1:
            return cost
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if not inside(nrow, ncol) or board[nrow][ncol] == -1:
                continue
            heapq.heappush(pq, (cost + board[nrow][ncol], nrow, ncol))
            board[nrow][ncol] = -1

seq = 1
while True:
    N = int(input())
    if N == 0:
        break
    board = [list(map(int, input().split())) for _ in range(N)]
    print(f'Problem {seq}: {solution(N, board)}')
    seq += 1