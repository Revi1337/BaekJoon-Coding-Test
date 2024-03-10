import sys
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(n, m, board):

    def bfs(row, col):
        distance = [[[0, 0] for _ in range(m)] for _ in range(n)]
        distance[row][col][0] = 1
        queue = deque([(row, col, 0)])
        while queue:
            row, col, break_cnt = queue.popleft()
            if (row, col) == (n - 1, m - 1):
                return distance[row][col][break_cnt]
            for d in range(4):
                nrow = row + drow[d]
                ncol = col + dcol[d]
                if (0 <= nrow < n) and (0 <= ncol < m):
                    if board[nrow][ncol] == 1 and break_cnt == 0:
                        distance[nrow][ncol][1] = distance[row][col][0] + 1
                        queue.append((nrow, ncol, 1))
                    if board[nrow][ncol] == 0 and distance[nrow][ncol][break_cnt] == 0:
                        distance[nrow][ncol][break_cnt] = distance[row][col][break_cnt] + 1
                        queue.append((nrow, ncol, break_cnt))
        return -1

    return bfs(0, 0)

n, m = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
print(solution(n, m, board))