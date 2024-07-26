import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, -1, 0, 1, 1, 1, 0, -1]
dcol = [0, 1, 1, 1, 0, -1, -1, -1]

def solution(w, h, board):

    answer = 0

    def bfs(r, c):
        board[r][c] = -1
        queue = deque([(r, c)])
        while queue:
            row, col = queue.popleft()
            for d in range(8):
                nrow = row + drow[d]
                ncol = col + dcol[d]
                if (0 <= nrow < h) and (0 <= ncol < w) and (board[nrow][ncol] == 1):
                    board[nrow][ncol] = -1
                    queue.append((nrow, ncol))

    for row in range(h):
        for col in range(w):
            if board[row][col] == 1:
                answer += 1
                bfs(row, col)

    return answer

while True:
    w, h = map(int, input().split())
    if  (w, h) == (0, 0):
        break
    board = [list(map(int, input().split())) for _  in range(h)]
    print(solution(w, h, board))
