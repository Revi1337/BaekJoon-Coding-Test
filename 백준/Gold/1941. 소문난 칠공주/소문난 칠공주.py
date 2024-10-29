import sys
from collections import deque

input = sys.stdin.readline

"""
소문난 칠공주 (https://www.acmicpc.net/problem/1941)
2024-10-01
"""

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(board):

    def visted():
        def bfs(r, c):
            queue = deque([(r, c)])
            v = [[0] * 5 for _ in range(5)]
            v[r][c] = 1
            cnt = 1
            while queue:
                row, col = queue.popleft()
                for d in range(4):
                    nrow, ncol = row + drow[d], col + dcol[d]
                    if (0 <= nrow < 5) and (0 <= ncol < 5) and (not v[nrow][ncol]) and (check[nrow][ncol]):
                        queue.append((nrow, ncol))
                        v[nrow][ncol] = 1
                        cnt += 1
            return cnt == 7

        for row in range(5):
            for col in range(5):
                if check[row][col] == 1:
                    return bfs(row, col)

    def backtrack(n, cnt, scnt):
        if cnt > 7:
            return
        if n == 25:
            if cnt == 7 and scnt >= 4:
                if visted():
                    nonlocal answer
                    answer += 1
            return
        check[n // 5][n % 5] = 1
        backtrack(n + 1, cnt + 1, scnt + int(board[n // 5][n % 5] == 'S'))
        check[n // 5][n % 5] = 0
        backtrack(n + 1, cnt, scnt)

    answer = 0
    check = [[0] * 5 for _ in range(5)]
    backtrack(0, 0, 0)
    print(answer)

board = [list(input().strip()) for _ in range(5)]
solution(board)
