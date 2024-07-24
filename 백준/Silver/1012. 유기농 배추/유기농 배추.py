import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(M, N, K, positions):
    answer = 0
    board = [[0] * M for _ in range(N)]
    for col, row in positions:
        board[row][col] = 1

    def bfs(r, c):
        queue = deque([(r, c)])
        board[r][c] = -1
        while queue:
            row, col = queue.popleft()
            for d in range(4):
                nrow, ncol = row + drow[d], col + dcol[d]
                if (0 <= nrow < N) and (0 <= ncol < M) and (board[nrow][ncol] == 1):
                    queue.append((nrow, ncol))
                    board[nrow][ncol] = -1

    for row in range(N):
        for col in range(M):
            if board[row][col] == 1:
                answer += 1
                bfs(row, col)

    print(answer)

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    positions = [list(map(int, input().split())) for _ in range(K)]
    solution(M, N, K, positions)
