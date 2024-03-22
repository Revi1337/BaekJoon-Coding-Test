from collections import deque
import sys

input = sys.stdin.readline

drow = [-1, 0, 1, 0]
dcol = [0, 1, 0, -1]

def solution(n, m, k, board):
    check = [[[0] * (k + 1) for _ in range(m)] for _ in range(n)]
    check[0][0][k] = 1
    queue = deque([(0, 0, k)])
    while queue:
        row, col, breaked = queue.popleft()
        if (row, col) == (n - 1, m - 1):
            return check[n - 1][m - 1][breaked]
        for d in range(4):
            nrow, ncol = row + drow[d], col + dcol[d]
            if (0 <= nrow < n) and (0 <= ncol < m):
                if board[nrow][ncol] == 1:
                    if (breaked > 0) and (not check[nrow][ncol][breaked - 1]):
                        check[nrow][ncol][breaked - 1] = check[row][col][breaked] + 1
                        queue.append((nrow, ncol, breaked - 1))
                else:
                    if not check[nrow][ncol][breaked]:
                        check[nrow][ncol][breaked] = check[row][col][breaked] + 1
                        queue.append((nrow, ncol, breaked))
    return -1

n, m, k = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(n)]
print(solution(n, m, k, board))