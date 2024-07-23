import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, board):
    queue = deque([(0, 0, 1)])
    board[0][0] = -1
    while queue:
        row, col, answer = queue.popleft()
        if (row, col) == (N - 1, M - 1):
            return answer
        for d in range(4):
            nrow = row + drow[d]
            ncol = col + dcol[d]
            if (0 <= nrow < N) and (0 <= ncol < M) and (board[nrow][ncol] == 1):
                board[nrow][ncol] = -1
                queue.append((nrow, ncol, answer + 1))

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
print(solution(N, M, board))