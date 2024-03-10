import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(n, m, board):

    answer = 0
    virus_positions = []

    def bfs():
        new_board = deepcopy(board)
        queue = deque()
        for row, col in virus_positions:
            queue.append([row, col])
        while queue:
            row, col = queue.popleft()
            for d in range(4):
                nrow = row + drow[d]
                ncol = col + dcol[d]
                if (0 <= nrow < n) and (0 <= ncol < m):
                    if new_board[nrow][ncol] == 0:
                        new_board[nrow][ncol] = 2
                        queue.append([nrow, ncol])

        counter = 0
        for row in range(n):
            for col in range(m):
                if new_board[row][col] == 0:
                    counter += 1
        nonlocal answer
        answer = max(answer, counter)

    def dfs(count):
        if count == 3:
            bfs()
            return
        for row in range(n):
            for col in range(m):
                if board[row][col] == 0:
                    board[row][col] = 1
                    dfs(count + 1)
                    board[row][col] = 0

    for row in range(n):
        for col in range(m):
            if board[row][col] == 2:
                virus_positions.append([row, col])

    dfs(0)

    return answer

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
print(solution(n, m, board))