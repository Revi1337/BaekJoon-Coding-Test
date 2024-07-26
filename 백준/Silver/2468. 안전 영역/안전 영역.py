import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, board):
    answer = -1e9
    nboard = [[0] * N for _ in range(N)]
    maxN = -1e9
    for line in board:
        maxN = max(maxN, max(line))

    def bfs(r, c):
        queue = deque([(r, c)])
        nboard[r][c] = -1
        while queue:
            row, col = queue.popleft()
            for d in range(4):
                nrow = row + drow[d]
                ncol = col + dcol[d]
                if (0 <= nrow < N) and (0 <= ncol < N) and (nboard[nrow][ncol] != -1):
                    nboard[nrow][ncol] = -1
                    queue.append((nrow, ncol))

    pre = 0
    for depth in range(maxN):
        for row in range(N):
            for col in range(N):
                if board[row][col] <= depth:
                    nboard[row][col] = -1
                else:
                    nboard[row][col] = board[row][col]
        for row in range(N):
            for col in range(N):
                if nboard[row][col] != -1:
                    pre += 1
                    bfs(row, col)

        answer = max(answer, pre)
        pre = 0

    return answer

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, board))

