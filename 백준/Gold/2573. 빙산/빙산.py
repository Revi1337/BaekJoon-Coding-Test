import sys
from collections import deque

input = sys.stdin.readline

"""
빙산 (https://www.acmicpc.net/problem/2573)
2024-09-12
"""

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(N, M, board):
    for year in range(1, 90000):
        tracking = []
        for row in range(1, N - 1):
            for col in range(1, M - 1):
                if board[row][col] > 0:
                    counter = 0
                    for d in range(4):
                        nr, nc = row + drow[d], col + dcol[d]
                        if board[nr][nc] == 0:
                            counter += 1
                    tracking.append((row, col, counter))
        for row, col, counter in tracking:
            if board[row][col] - counter <= 0:
                board[row][col] = 0
            else:
                board[row][col] -= counter

        counter = 0
        check = set()
        for row in range(1, N - 1):
            for col in range(1, M - 1):
                if board[row][col] > 0 and (row, col) not in check:
                    counter += 1
                    check.add((row, col))
                    queue = deque([(row, col)])
                    while queue:
                        r, c = queue.popleft()
                        for d in range(4):
                            nr, nc = r + drow[d], c + dcol[d]
                            if board[nr][nc] > 0 and (nr, nc) not in check:
                                check.add((nr, nc))
                                queue.append((nr, nc))
                    if counter >= 2:
                        return year
        if counter == 0:
            return 0

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
print(solution(N, M, board))
