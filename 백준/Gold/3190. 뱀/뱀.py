import sys
from collections import deque

input = sys.stdin.readline

drow = [0, 1, 0, -1]
dcol = [1, 0, -1, 0]

def solution(n, k, apple, l, d):
    time_dict = {int(key): value for (key, value) in d}
    board = [[0] * (n + 1) for _ in range(n + 1)]
    for row, col in apple:
        board[row][col] = 1

    nrow, ncol, dir = 1, 1, 0
    snake = deque()
    sec = 0
    while True:
        snake.append((nrow, ncol))
        sec += 1

        nrow += drow[dir]
        ncol += dcol[dir]

        if nrow < 1 or nrow >= n + 1 or ncol < 1 or ncol >= n + 1 or board[nrow][ncol] == 2:
            break

        if not board[nrow][ncol]:
            i, j = snake.popleft()
            board[i][j] = 0

        board[nrow][ncol] = 2

        if sec in time_dict:
            if time_dict[sec] == 'D':
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4
    return sec

n = int(input().rstrip())
k = int(input().rstrip())
apple = [list(map(int, input().split())) for _ in range(k)]
l = int(input().rstrip())
d = [input().rstrip().split() for _ in range(l)]
print(solution(n, k, apple, l, d))
